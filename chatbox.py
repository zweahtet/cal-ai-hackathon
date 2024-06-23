import time
import json
import streamlit as st
from typing import Dict, List, Any
from crew import SentimentCrew
import re
import json
import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API"),
)


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

                    message_content = "The user input is as follows: {} , please give me the name of the company company_name and date_start date_end and output as a json formatted string ONLY. We will need mm-dd-yyyy. I'm not asking for a script, just give me the JSON.".format(
                        prompt
                    )

                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": message_content,
                            }
                        ],
                        model="llama3-8b-8192",
                    )

                    result = chat_completion.choices[0].message.content
                    # Regular expression to find JSON objects
                    json_pattern = re.compile(r"\{.*?\}", re.DOTALL)

                    # Find all JSON objects in the string
                    json_matches = json_pattern.findall(result)

                    # Parse the JSON objects and extract values
                    elements_list = []

                    for json_str in json_matches:
                        try:
                            data = json.loads(json_str)
                            elements_list.extend(data.values())
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON: {e}")

                    print(elements_list)

                    company_name, date_start, date_end = elements_list
                    sentiment_crew = SentimentCrew(
                        company_name, f"{date_start} to {date_end}"
                    )
                    ai_response = sentiment_crew.run()

                except Exception as e:
                    ai_response = f"An error occurred: {e}"

                st.write(ai_response)

                st.session_state["ai_messages"].append(
                    {"role": "assistant", "content": ai_response}
                )
