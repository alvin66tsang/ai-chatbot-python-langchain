from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory


# session storage
session_store = {}

def get_session_history(session_id):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

def get_chat_response(input_prompt, session_id, openai_api_key):
    model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | model

    with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    response = with_history.invoke({
        "input": input_prompt,
    },
        config=RunnableConfig(configurable= {"session_id": session_id})
    )
    return response.content
