from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import AIAgent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize AI Agent
agent = AIAgent()

@app.route('/', methods=['GET'])
def home():
    return {'message': 'AI Agent API is running'}

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Get response from AI agent
        response = agent.process_message(user_message)
        
        return jsonify({
            'success': True,
            'message': user_message,
            'response': response
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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