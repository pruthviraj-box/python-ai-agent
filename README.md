# Python AI Agent with Web UI

A Python AI agent with a browser chat interface and a random joke generator powered by the [Official Joke API](https://official-joke-api.appspot.com/).

## Features

- 🤖 AI-powered chat using LangChain and OpenAI GPT-3.5-turbo
- 💬 Responsive browser chat UI
- 🧠 Conversation memory
- 🛠️ Built-in agent tools for time, calculations, and information lookup
- 🎲 Random joke generator using an external API
- 📱 Mobile-friendly layout

## Installation

```bash
git clone https://github.com/pruthviraj-box/python-ai-agent.git
cd python-ai-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
```

Add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

Start the Flask API:

```bash
python app.py
```

Then serve the UI from the project directory in another terminal:

```bash
python -m http.server 8000
```

Open http://localhost:8000 and click **Get a joke**. The browser calls the Flask `/api/joke` endpoint, which fetches a joke server-side from the Official Joke API and returns it to the UI.

## API endpoints

### `GET /api/joke`

Returns a random joke from the external API:

```json
{
  "success": true,
  "id": 42,
  "type": "twopart",
  "joke": "Why did the chicken cross the road?\\n\\nTo get to the other side."
}
```

The backend returns a friendly `502` error if the external service is unavailable or returns invalid data.

### `POST /api/chat`

Send a message to the AI agent:

```json
{ "message": "What time is it?" }
```

### `POST /api/reset`

Clear the current conversation memory.

### `GET /api/history`

Return the current in-memory conversation history.
