### AI Chatbot with LangChain & Streamlit

A modern, stateful AI conversational assistant built with Python 3.11+, LangChain, and Streamlit. This bot features persistent session memory, allowing it to remember context throughout a conversation.

## Features
1. Persistent Memory: Utilizes RunnableWithMessageHistory to maintain context across multiple turns.
2. Session Management: Sidebar integration to reset the conversation and start a "New Chat" instantly.
3. Secure API Handling: Input your OpenAI API Key directly into the UI (processed via Pydantic SecretStr).
4. Interactive UI: Built with Streamlit's native st.chat_message and st.chat_input components.

## Getting Started
1. Prerequisites
Ensure you have Python installed (3.10 or higher recommended). You will also need an OpenAI API Key.

2. Installation
Clone this repository and install the required dependencies:
git clone https://github.com/alvin66tsang/ai-chatbot-python-langchain.git
cd aichatbot
pip install -r requirements.txt

3. Running the App
Launch the Streamlit server from your terminal:
streamlit run main.py

## How to Use
Authentication: Once the web page opens, locate the sidebar or input field to Insert your OpenAI API Key.
Chatting: Type your message into the text box at the bottom of the screen and press Enter.
Memory: The AI will remember details from earlier in the conversation (e.g., "My name is Alex" ... "What is my name?").
Resetting: To clear the current history and start fresh, click the "New Chat" button located in the sidebar.