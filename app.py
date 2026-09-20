from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import AIAgent
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize AI Agent
agent = AIAgent()

JOKE_API_URL = 'https://official-joke-api.appspot.com/random_joke'

@app.route('/', methods=['GET'])
def home():
    return {'message': 'AI Agent API is running'}

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Message is required'}), 400

        response = agent.process_message(user_message)

        return jsonify({
            'success': True,
            'message': user_message,
            'response': response
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/joke', methods=['GET'])
def get_joke():
    """Fetch a random joke from the Official Joke API."""
    try:
        response = requests.get(JOKE_API_URL, timeout=8)
        response.raise_for_status()
        joke = response.json()

        if joke.get('type') == 'single':
            text = joke.get('joke', '')
        else:
            setup = joke.get('setup', '')
            punchline = joke.get('punchline', '')
            text = f'{setup}\n\n{punchline}'

        if not text.strip():
            return jsonify({'error': 'The joke API returned an empty joke'}), 502

        return jsonify({
            'success': True,
            'id': joke.get('id'),
            'type': joke.get('type'),
            'joke': text
        })
    except requests.RequestException:
        return jsonify({'error': 'Unable to fetch a joke right now. Please try again.'}), 502
    except (TypeError, ValueError):
        return jsonify({'error': 'The joke API returned an invalid response.'}), 502

@app.route('/api/reset', methods=['POST'])
def reset():
    try:
        agent.reset_memory()
        return jsonify({'success': True, 'message': 'Conversation reset'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        history = agent.get_conversation_history()
        return jsonify({'success': True, 'history': history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
