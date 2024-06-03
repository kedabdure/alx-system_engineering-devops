#!/usr/bin/python3
"""
gather data from API and export it to CSV file
"""

import requests
import sys

API = "https://jsonplaceholder.typicode.com"
"""REST API url to fetch data"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a numeric value.")
        sys.exit(1)

    user_res = requests.get(f'{API}/users/{employee_id}')
    todo_res = requests.get(f'{API}/todos?userId={employee_id}')

    if user_res.status_code != 200:
        print("Error fetching user data")
        sys.exit(1)

    if todo_res.status_code != 200:
        print("Error fetching TODO data")
        sys.exit(1)

    user_data = user_res.json()
    todos_data = todo_res.json()

    username = user_data.get('username')
    todos = [todo for todo in todos_data if todo['userId'] == employee_id]

    file_name = f"{employee_id}.csv"
    with open(file_name, 'w') as file:
        for todo in todos:
            file.write(
                '"{}","{}","{}","{}"\n'.format(
                    employee_id,
                    username,
                    todo['completed'],
                    todo['title']
                )
            )
