import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# ----------------------------
# Load env
# ----------------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY missing in .env")
    st.stop()

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Context-Aware Gemini Chatbot")
st.write("Type below to chat. Context is remembered in this session.")

# ----------------------------
# LLM
# ----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",   # Stable working model
    temperature=0.5,
    google_api_key=API_KEY,
)

# ----------------------------
# Prompt
# ----------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, friendly assistant. Remember conversation context."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

# ----------------------------
# Session-based memory
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = InMemoryChatMessageHistory()

def get_session_history(session_id: str):
    return st.session_state.history

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# ----------------------------
# Chat UI
# ----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    response = chatbot.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "default"}}
    )

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response.content)
