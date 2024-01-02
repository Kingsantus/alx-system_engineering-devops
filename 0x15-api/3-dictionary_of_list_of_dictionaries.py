#!/usr/bin/python3
""" Uses REST API to return information about all employees
    Exports employee records to a JSON file
"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    all_employees_data = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    data = {}

    for employee_data in all_employees_data:
        userID = employee_data.get("id")
        userName = employee_data.get("username")
        task_list = []

        for task in todos:
            id = task.get("userId")
            task_title = task.get("title")
            task_status = task.get("completed")
            if userID == id:
                task_description = {
                    "username": userName,
                    "task": task_title,
                    "completed": task_status,
                    }
                task_list.append(task_description)

        data[str(userID)] = task_list

    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="UTF-8") as file:
        json.dump(data, file)
