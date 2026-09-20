const chatBox = document.getElementById('chatBox');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const resetBtn = document.getElementById('resetBtn');
const jokeBtn = document.getElementById('jokeBtn');
const jokeText = document.getElementById('jokeText');
const loadingIndicator = document.getElementById('loadingIndicator');

const API_URL = 'http://localhost:5000/api';

sendBtn.addEventListener('click', sendMessage);
jokeBtn.addEventListener('click', getRandomJoke);

userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

resetBtn.addEventListener('click', resetChat);

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    userInput.value = '';
    addMessage(message, 'user');
    setChatLoading(true);

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'The agent could not respond.');
        }
        addMessage(data.response, 'agent');
    } catch (error) {
        console.error('Chat error:', error);
        addMessage(`Error: ${error.message}`, 'agent');
    } finally {
        setChatLoading(false);
        userInput.focus();
    }
}

async function getRandomJoke() {
    jokeBtn.disabled = true;
    jokeText.textContent = 'Fetching a fresh joke...';

    try {
        const response = await fetch(`${API_URL}/joke`);
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || 'Unable to fetch a joke.');
        }
        jokeText.textContent = data.joke;
    } catch (error) {
        console.error('Joke error:', error);
        jokeText.textContent = error.message;
    } finally {
        jokeBtn.disabled = false;
    }
}

function setChatLoading(isLoading) {
    loadingIndicator.classList.toggle('hidden', !isLoading);
    sendBtn.disabled = isLoading;
}

function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const paragraph = document.createElement('p');
    paragraph.textContent = message;
    messageDiv.appendChild(paragraph);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function resetChat() {
    if (!confirm('Are you sure you want to reset the conversation?')) return;

    try {
        const response = await fetch(`${API_URL}/reset`, { method: 'POST' });
        if (!response.ok) throw new Error('Unable to reset the conversation.');
        chatBox.innerHTML = '<div class="message agent-message"><p>Conversation reset. How can I help you?</p></div>';
    } catch (error) {
        console.error('Reset error:', error);
    }
}

window.addEventListener('load', () => userInput.focus());
