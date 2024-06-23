import time
import json
import streamlit as st
from typing import Dict, List, Any

def show_previous_messages(messages_container: any):
    with messages_container:
        messages: List[Dict[str, Any]] = st.session_state["ai_messages"]
        for message in messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


def show_chat_input(
    disabled: bool,  messages_container: any
):
    if disabled:
        st.info("Make sure to select a model and file to start chatting!")

    if prompt := st.chat_input("Say something", disabled=disabled):
        st.session_state["ai_messages"].append(
            {"role": "user", "content": prompt}
        )

        with messages_container:
            with st.chat_message("user"):
                st.write(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        ai_response = model.get_response(
                            query_str=prompt,
                            chat_history=st.session_state["ai_messages"],
                        )
                        # when streaming, the response format is gone
                        # ai_response = model.get_stream_response(
                        #     query_str=prompt,
                        #     chat_history=st.session_state[f"{framework}_chat_history"],
                        # )
                    except Exception as e:
                        ai_response = f"An error occurred: {e}"

                    st.write(ai_response)
                    # response = st.write_stream(ai_response)

                    st.session_state["ai_messages"].append(
                        {"role": "assistant", "content": ai_response}
                    )
