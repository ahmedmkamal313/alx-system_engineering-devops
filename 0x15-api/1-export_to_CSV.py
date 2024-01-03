#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    employee_id = sys.argv[1]
    # Define the base URL of the API
    url = "https://jsonplaceholder.typicode.com/"
    # Send a GET request to the API to get the user data
    user = requests.get(f"{url}users/{employee_id}").json()
    # Get the username from the user data
    username = user.get("username")
    # Send another GET request to the API to get
    # the todos data with the employee ID as a parameter
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()

    # Open a CSV file with the employee ID as the name
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        # Create a DictWriter object with the field names and quoting option
        writer = csv.DictWriter(
                csvfile, fieldnames=[
                    "USER_ID", "USERNAME",
                    "TASK_COMPLETED_STATUS",
                    "TASK_TITLE"
                    ], quoting=csv.QUOTE_ALL
                )
        # Write the header row to the CSV file
        writer.writeheader()
        # Iterate over the todos data
        for todo in todos:
            # Write each todo as a dictionary to the CSV file
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": todo.get("completed"),
                "TASK_TITLE": todo.get("title")
            })
