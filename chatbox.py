import time
import json
import streamlit as st
from typing import Dict, List, Any
from crew import SentimentCrew


def show_previous_messages(messages_container: any):
    with messages_container:
        messages: List[Dict[str, Any]] = st.session_state["ai_messages"]
        for message in messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


def show_chat_input(disabled: bool, messages_container: any):

    if prompt := st.chat_input("Say something", disabled=disabled):
        st.session_state["ai_messages"].append({"role": "user", "content": prompt})

        with messages_container:
            with st.chat_message("user"):
                st.write(prompt)

            with st.chat_message("assistant"):
                try:
                    # ai_response = model.get_response(
                    #     query_str=prompt,
                    #     chat_history=st.session_state["ai_messages"],
                    # )
                    sentiment_crew = SentimentCrew("Apple", "01-01-2022 to 03-01-2022")
                    ai_response = sentiment_crew.run()

                except Exception as e:
                    ai_response = f"An error occurred: {e}"

                st.write(ai_response)

                st.session_state["ai_messages"].append(
                    {"role": "assistant", "content": ai_response}
                )
