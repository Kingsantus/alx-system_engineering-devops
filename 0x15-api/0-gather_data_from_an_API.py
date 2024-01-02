#!/usr/bin/python3
""" Uses REST API to return information about an employee """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 module_name.py ID")
        sys.exit(1)

    ID = int(sys.argv[1])
    if not isinstance(ID, int):
        print("ID must be an integer")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_data = requests.get(url + "users/{}".format(ID)).json()
    todos = requests.get(url + "todos", params={"userId": ID}).json()

    completed_tasks = [todo.get("title") for todo
                       in todos if todo.get("completed") is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        (employee_data.get("name")), len(completed_tasks), total_tasks))
    [print("\t {}".format(task)) for task in completed_tasks]
