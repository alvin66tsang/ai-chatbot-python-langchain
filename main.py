import streamlit as st
import os
import uuid
from utils import get_chat_response
from dotenv import load_dotenv

load_dotenv()

st.title("AI Chatbot")

with st.sidebar:
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password", value=os.getenv("OPENAI_API_KEY"))
    st.markdown("[Get your API Key here](https://platform.openai.com/api-keys)")
    if st.button("New Chat"):
        st.session_state.clear()

    ### define history session id and initialize message
if "memory" not in st.session_state:
    st.session_state["memory"] = str(uuid.uuid4())
    st.session_state["messages"] = [
        {"role": "ai", "content": "Hi, I am your AI assistant! What can i do with you?"},
    ]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()

if prompt:
    # Not runnable if no api key
    if not openai_api_key:
        st.info("API Key not provided or Nothing in prompt")
        st.stop()
    # Running the request
    st.session_state["messages"].append(
        {"role": "human", "content": prompt}
    )
    st.chat_message("human").write(prompt)

    with st.spinner(text="Thinking...", show_time=True):
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key)

    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message(msg["role"]).write(msg["content"])

