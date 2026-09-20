import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool
from datetime import datetime


class AIAgent:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = ChatOpenAI(
            temperature=0.7,
            openai_api_key=self.api_key,
            model_name='gpt-3.5-turbo'
        )
        self.memory = ConversationBufferMemory(memory_key='chat_history')
        self.conversation_history = []
        self._initialize_agent()
    
    def _initialize_agent(self):
        """Initialize the agent with tools"""
        tools = [
            self.get_current_time,
            self.calculate,
            self.search_info
        ]
        
        self.agent_chain = initialize_agent(
            tools,
            self.model,
            agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )
    
    @tool
    def get_current_time():
        """Get the current date and time"""
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    @tool
    def calculate(expression: str) -> str:
        """Evaluate a mathematical expression"""
        try:
            result = eval(expression)
            return str(result)
        except:
            return "Invalid expression"
    
    @tool
    def search_info(query: str) -> str:
        """Search for information (simulated)"""
        return f"Information about: {query}"
    
    def process_message(self, user_message: str) -> str:
        """Process user message and return agent response"""
        try:
            response = self.agent_chain.run(input=user_message)
            
            # Store in conversation history
            self.conversation_history.append({
                'timestamp': datetime.now().isoformat(),
                'user': user_message,
                'agent': response
            })
            
            return response
        except Exception as e:
            error_msg = f"Error processing message: {str(e)}"
            print(error_msg)
            return error_msg
    
    def reset_memory(self):
        """Reset conversation memory"""
        self.memory.clear()
        self.conversation_history = []
    
    def get_conversation_history(self) -> list:
        """Get conversation history"""
        return self.conversation_history