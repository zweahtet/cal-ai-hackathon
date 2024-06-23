import json
import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_attribute(data, attribute):
    return [item["Tweet_Content"] for item in data if "Tweet_Content" in item]

positive_emotions = ["Admiration", "Adoration", "Aesthetic Appreciation", "Amusement", "Awe", "Ecstasy", "Enthusiasm", "Excitement", "Gratitude", "Joy", "Interest", "Satisfaction", "Surprise (positive)", "Triumph"]
results = []
finalResults = []
client = HumeStreamClient("texVIA2o5o60QaXUxvXGnrv3DHKKOoiQr7d5EHE3SYBAKGVg")
config = LanguageConfig()

async def calculate_rating(post):
    async with client.connect([config]) as socket:
          result = await socket.send_text(post)
          emotions = result["language"]["predictions"][0]["emotions"]
          results.append(emotions)
          rating = 0
          for expression in emotions:
               key = expression["name"]
               value = expression["score"]
               if key in positive_emotions:
                    rating += value
          finalResults.append(rating)
          return rating

if __name__ == "__main__":
    # File path to the JSON file
    file_path = 'chevron.json' # INPUT: Change this to the path of your JSON file

    # Read JSON data from the file
    json_data = read_json_file(file_path)

    # Extract a specific attribute (e.g., 'name') from each element
    attribute = 'name'
    attribute_list = extract_attribute(json_data, attribute)

    # Print the list of extracted attributes
    for item in attribute_list:
        # asyncio.run(main())
        print(asyncio.run(calculate_rating(item)))




""" WRITE TO FILE
    # Define the file name
    file_name = "my_list.txt"

    # Write the updated list to a text file
    with open(file_name, "w") as file:
        for item in finalResults:
            file.write(f"{item}\n")

    print(f"Updated list has been written to {file_name}")
    """

