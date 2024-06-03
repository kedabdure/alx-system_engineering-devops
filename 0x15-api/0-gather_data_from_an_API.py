#!/usr/bin/python3
"""
Fetches and displays TODO list progress using the JSONPlaceholder API.
"""

import requests
import sys

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


def display_todo_progress(employee_id):
    """Display the TODO list progress for the employee."""
    try:
        user_data, todos_data = fetch_employee_data(employee_id)
    except Exception as e:
        print(e)
        return

    e_m = user_data.get('name')
    c_t = [todo['title'] for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)
    d_t_c = len(c_t)

    print(f"Employee {e_m} is done with tasks ({d_t_c}/{total_tasks}):")
    for task in c_t:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a numeric value.")
        sys.exit(1)

    display_todo_progress(employee_id)
