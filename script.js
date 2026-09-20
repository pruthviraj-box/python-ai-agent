const chatBox = document.getElementById('chatBox');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const resetBtn = document.getElementById('resetBtn');
const loadingIndicator = document.getElementById('loadingIndicator');

const API_URL = 'http://localhost:5000/api';

// Send message on button click
sendBtn.addEventListener('click', sendMessage);

// Send message on Enter key
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Reset chat
resetBtn.addEventListener('click', resetChat);

async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message) return;
    
    // Clear input
    userInput.value = '';
    
    // Add user message to chat
    addMessage(message, 'user');
    
    // Show loading indicator
    loadingIndicator.classList.remove('hidden');
    sendBtn.disabled = true;
    
    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            addMessage(data.response, 'agent');
        } else {
            addMessage(`Error: ${data.error}`, 'agent');
        }
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, I encountered an error. Please check if the server is running.', 'agent');
    } finally {
        loadingIndicator.classList.add('hidden');
        sendBtn.disabled = false;
        userInput.focus();
    }
}

function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const paragraphDiv = document.createElement('p');
    paragraphDiv.textContent = message;
    
    messageDiv.appendChild(paragraphDiv);
    chatBox.appendChild(messageDiv);
    
    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function resetChat() {
    if (!confirm('Are you sure you want to reset the conversation?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/reset`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        if (response.ok) {
            chatBox.innerHTML = '<div class="message agent-message"><p>Conversation reset. How can I help you?</p></div>';
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Focus input on load
window.addEventListener('load', () => {
    userInput.focus();
});