#!/usr/bin/python3
""" Uses REST API to return information about an employee
    Exports employee records to a JSON file
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 module_name.py ID")
        sys.exit(1)

    ID = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/"
    employee_data = requests.get(url + "users/{}".format(ID)).json()
    todos = requests.get(url + "todos", params={"userId": ID}).json()

    userName = employee_data.get("username")

    task_list = []
    for task in todos:
        task_title = task.get("title")
        task_status = task.get("completed")
        task_description = {
            "task": task_title,
            "completed": task_status,
            "username": userName
            }
        task_list.append(task_description)
    data = {str(ID): task_list}

    filename = f"{ID}.json"
    with open(filename, mode="w", encoding="UTF-8") as file:
        json.dump(data, file)
