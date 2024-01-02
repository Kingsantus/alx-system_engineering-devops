#!/usr/bin/python3
""" Uses REST API to return information about an employee
    Exports employee records to a csv file
"""
import csv
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

    userName = employee_data.get("username")
    task_status = [task.get("completed") for task in todos]
    task_title = [title.get("title") for title in todos]

    rows = zip([ID] * len(task_title), [userName] * len(task_title),
               task_status, task_title)

    filename = f"{ID}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
