import requests

# OCTOPARSE API Demo
# This script demonstrates how to get access token and 
# get non-exported data from Octoparse API for X results.

# Constants
BASE_URL = "https://openapi.octoparse.com"
USERNAME = "your_username"
PASSWORD = "your_password"

def get_access_token(username, password):
    url = f"{BASE_URL}/token"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "username": username,
        "password": password,
        "grant_type": "password"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.json()}")

def get_non_exported_data(access_token, task_id, size):
    url = f"{BASE_URL}/data/notexported?taskId={task_id}&size={size}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        raise Exception(f"Failed to get data: {response.json()}")

def main():
    # Get Access Token
    access_token = get_access_token(USERNAME, PASSWORD)
    print(f"Access Token: {access_token}")

    # Get Non-Exported Data
    task_id = "your_task_id"
    size = 10
    data = get_non_exported_data(access_token, task_id, size)
    print(f"Data: {data}")
