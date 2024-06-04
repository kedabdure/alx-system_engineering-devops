#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
"""

import json
import requests

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_data(endpoint):
    """Fetch data from the API endpoint."""
    response = requests.get(f"{API_URL}/{endpoint}")
    if response.status_code != 200:
        raise Exception(f"Error fetching data from {endpoint}")
    return response.json()


def main():
    """Main function to fetch user and todo data and export it to a JSON file."""
    try:
        users = fetch_data("users")
        todos = fetch_data("todos")
    except Exception as e:
        print(e)
        return

    all_users_data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        
        # Filter todos for the current user
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        
        user_tasks = [
            {
                'username': username,
                'task': todo.get('title'),
                'completed': todo.get('completed')
            }
            for todo in user_todos
        ]
        
        all_users_data[user_id] = user_tasks

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users_data, json_file, indent=4)

    print("Data for all employees has been exported to todo_all_employees.json")


if __name__ == '__main__':
    main()
