import os
import re
import json

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

user_input = input("Enter user input: ")

message_content = "The user input is as follows: {} , please give me the name of the company company_name and date_start date_end and output as a json formatted string ONLY. We will need mm-dd-yyyy. I'm not asking for a script, just give me the JSON.".format(user_input)

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
print(result)
# Regular expression to find JSON objects
json_pattern = re.compile(r'\{.*?\}', re.DOTALL)

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
