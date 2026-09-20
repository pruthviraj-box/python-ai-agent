# Python AI Agent with Web UI

A powerful AI agent built with Python that features a modern web-based chat interface. The agent can understand natural language, maintain conversation context, and perform various tasks.

## Features

- 🤖 **AI-Powered Agent** - Uses LangChain and OpenAI GPT-3.5-turbo
- 💬 **Real-time Chat Interface** - Modern, responsive web UI
- 🧠 **Conversation Memory** - Maintains context across messages
- 🛠️ **Built-in Tools** - Get current time, calculate expressions, search info
- 📱 **Mobile-Friendly** - Works on desktop and mobile devices
- 🔄 **Conversation History** - View and manage chat history

## Prerequisites

- Python 3.8+
- OpenAI API Key
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pruthviraj-box/python-ai-agent.git
   cd python-ai-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. **Start the backend server**
   ```bash
   python app.py
   ```
   
   The server will run on `http://localhost:5000`

2. **Open the web UI**
   - Open `index.html` in your web browser or
   - Serve it with a simple HTTP server:
     ```bash
     python -m http.server 8000
     ```
   - Then visit `http://localhost:8000`

3. **Start chatting**
   - Type your message in the input field
   - Press Enter or click the Send button
   - The AI agent will respond with relevant information

## Project Structure

```
python-ai-agent/
├── app.py              # Flask backend server
├── agent.py            # AI Agent logic
├── requirements.txt    # Python dependencies
├── index.html          # Web UI (HTML)
├── style.css           # UI styling
├── script.js           # UI interactions
├── .env.example        # Environment variables template
└── README.md           # This file
```

## API Endpoints

### POST `/api/chat`
Send a message to the AI agent.

**Request:**
```json
{
  "message": "What time is it?"
}
```

**Response:**
```json
{
  "success": true,
  "message": "What time is it?",
  "response": "The current time is 2024-01-15 14:30:45"
}
```

### POST `/api/reset`
Reset the conversation and clear memory.

**Response:**
```json
{
  "success": true,
  "message": "Conversation reset"
}
```

### GET `/api/history`
Get the conversation history.

**Response:**
```json
{
  "success": true,
  "history": [
    {
      "timestamp": "2024-01-15T14:30:00",
      "user": "What time is it?",
      "agent": "The current time is 2024-01-15 14:30:45"
    }
  ]
}
```

## Agent Capabilities

The AI agent comes with built-in tools:

- **Get Current Time** - Returns the current date and time
- **Calculate** - Evaluates mathematical expressions
- **Search Info** - Searches for information (extendable)

## Customization

### Adding New Tools

Edit `agent.py` and add new tools in the `_initialize_agent` method:

```python
@tool
def your_custom_tool(input: str) -> str:
    """Description of your tool"""
    # Your implementation
    return result
```

### Changing the Model

Edit `agent.py` to use a different OpenAI model:

```python
self.model = ChatOpenAI(
    model_name='gpt-4'  # Change to gpt-4 or another model
)
```

## Troubleshooting

### "Connection refused" error
- Make sure the Flask server is running on port 5000
- Check if the port is already in use

### "Invalid API key" error
- Verify your OpenAI API key in the `.env` file
- Make sure you have valid credits in your OpenAI account

### CORS errors
- Make sure Flask-CORS is installed
- Check that the API_URL in `script.js` matches your server address

## Future Enhancements

- [ ] Add more advanced tools and integrations
- [ ] Implement user authentication
- [ ] Add database support for persistent conversations
- [ ] Deploy to cloud (AWS, Heroku, etc.)
- [ ] Add voice input/output
- [ ] Implement multi-user support

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.
