#!/usr/bin/python3
"""
Fetches and exports user TODO data to a JSON file.
"""

import json
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def get_user_and_todos(user_id):
    """Fetch user and todos data for a given user ID."""
    user_resp = requests.get(f"{API_URL}/users/{user_id}")
    todos_resp = requests.get(f"{API_URL}/todos", params={"userId": user_id})

    if user_resp.status_code != 200 or todos_resp.status_code != 200:
        raise Exception("Error fetching data")

    user = user_resp.json()
    todos = todos_resp.json()
    return user, todos


def save_to_json(user_id, username, todos):
    """Save user TODO data to a JSON file."""
    tasks = [
        {"task": todo["title"], "completed": todo["completed"],
         "username": username}
        for todo in todos
    ]
    with open(f"{user_id}.json", 'w') as file:
        json.dump({str(user_id): tasks}, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    try:
        user, todos = get_user_and_todos(user_id)
        save_to_json(user_id, user['username'], todos)
    except Exception as e:
        print(e)
        sys.exit(1)
