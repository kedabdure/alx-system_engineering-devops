#!/usr/bin/python3
"""
Fetches data from the JSONPlaceholder API and exports it to a JSON file.
"""
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_data(endpoint):
    """Fetch data from the provided endpoint."""
    response = requests.get(f"{BASE_URL}/{endpoint}")
    response.raise_for_status()
    return response.json()


def main():
    users = fetch_data("users")
    todos = fetch_data("todos")

    user_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        user_todos = [
            {
                'username': username,
                'task': todo['title'],
                'completed': todo['completed']
            }
            for todo in todos if todo['userId'] == user_id
        ]

        user_tasks[user_id] = user_todos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file, indent=4)


if __name__ == "__main__":
    main()
