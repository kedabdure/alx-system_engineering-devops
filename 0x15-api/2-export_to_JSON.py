#!/usr/bin/python3
"""
Fetches and displays TODO list progress using the JSONPlaceholder API.
Exports data to a JSON file.
"""

import requests
import sys
import json

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_employee_data(employee_id):
    """Fetch employee and TODO data from the API."""
    user_response = requests.get(f"{API_URL}/users/{employee_id}")
    todos_response = requests.get(f"{API_URL}/todos?userId={employee_id}")

    if user_response.status_code != 200:
        raise Exception("Error fetching user data")
    if todos_response.status_code != 200:
        raise Exception("Error fetching TODO data")

    return user_response.json(), todos_response.json()


def export_to_json(employee_id):
    """Export the TODO list progress for the employee to a JSON file."""
    try:
        user_data, todos_data = fetch_employee_data(employee_id)
    except Exception as e:
        print(e)
        return

    username = user_data.get('username')
    tasks = [
        {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        } for todo in todos_data
    ]

    json_data = {str(employee_id): tasks}
    
    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data for employee ID {employee_id} has been exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a numeric value.")
        sys.exit(1)

    export_to_json(employee_id)
