#!/usr/bin/python3
"""
Fetches and displays TODO list progress using the JSONPlaceholder API.
Exports data to a JSON file.
"""

import requests
import json

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_all_data():
    """Fetch all user and TODO data from the API."""
    users_response = requests.get(f"{API_URL}/users")
    todos_response = requests.get(f"{API_URL}/todos")

    if users_response.status_code != 200:
        raise Exception("Error fetching users data")
    if todos_response.status_code != 200:
        raise Exception("Error fetching TODO data")

    return users_response.json(), todos_response.json()


def export_all_to_json():
    """Export all TODO list progress for all employees to a JSON file."""
    try:
        users_data, todos_data = fetch_all_data()
    except Exception as e:
        print(e)
        return

    all_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            } for todo in todos_data if todo['userId'] == user_id
        ]
        all_tasks[user_id] = user_tasks

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)

    print(f"Data for all employees has been exported to {file_name}")


if __name__ == "__main__":
    export_all_to_json()
