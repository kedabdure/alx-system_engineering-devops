#!/usr/bin/python3
"""modole for fetch api"""
import requests
import sys


API = 'https://jsonplaceholder.typicode.com'


def get_employee_data(employee_id):
    """fetch user and todo list data"""
    user_url = f"{API}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        raise Exception(f"Failed to fetch user data: {user_response.status_code}")
    user_data = user_response.json()

    todos_url = f"{API}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        raise Exception(f"Failed to fetch TODO data: {todos_response.status_code}")
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(employee_id):
    """display the data"""
    try:
        user, todos = get_employee_data(employee_id)
    except Exception as e:
        print(e)
        return

    employee_name = user['name']
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a numeric value.")
        sys.exit(1)

    display_todo_progress(employee_id)
