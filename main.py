import streamlit as st
from chatbox import show_previous_messages, show_chat_input

def init_session_state():
    if "ai_messages" not in st.session_state:
        st.session_state.ai_messages = [
            {"role": "assistant", "content": "How can I help you today?"}
        ]

init_session_state()

st.set_page_config(page_title="EcoMetrics", page_icon="📜🤖")
st.title("Welcome to EcoMetrics")
st.header("Built with `Langchain🦜🔗`, `Hume.ai`, `Groq` and `Streamlit`")

messages_container = st.container(height=300)
show_previous_messages(messages_container=messages_container)
show_chat_input(
    disabled=False,
    messages_container=messages_container,
)

def clear_history():
    messages_container.empty()
    st.session_state.ai_messages = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]

if st.button("Clear Chat History"):
    clear_history()
    st.rerun()
