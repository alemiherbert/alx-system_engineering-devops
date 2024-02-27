#!/usr/bin/python3
"""This script collects data from an API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if task.get("completed") is True]
    print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")
    [print("\t " + task) for task in completed]