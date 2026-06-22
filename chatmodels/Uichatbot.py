import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

# Mode Selection
mode_option = st.selectbox(
    "Choose your mode of response",
    ["Angry", "Funny", "Sad"]
)

if mode_option == "Angry":
    mode = "you are Angry ai agent"
elif mode_option == "Funny":
    mode = "you are funny ai agent"
else:
    mode = "you are sad ai agent"

# Initialize session state
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if st.session_state.current_mode != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(msg)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.chat_history.append(("user", prompt))
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = llm.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.session_state.chat_history.append(
        ("assistant", response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)