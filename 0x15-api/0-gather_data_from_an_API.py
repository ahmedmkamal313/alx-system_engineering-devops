#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

# Import requests module
import requests
# Import sys module to get command line arguments
import sys

# Get the employee ID from the first argument
employee_id = sys.argv[1]

# Define the API URL
api_url = "https://jsonplaceholder.typicode.com/todos"

# Make a GET request to the API with the employee ID as a parameter
response = requests.get(api_url, params={"userId": employee_id})

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Get the employee name from the first item in the data
    employee_name = data[0]["user"]["name"]

    # Get the total number of tasks
    total_tasks = len(data)

    # Get the number of completed tasks
    completed_tasks = sum(task["completed"] for task in data)

    # Print the first line of the output
    print(
            "Employee {} is done with tasks({}/{})"
            .format(employee_name, completed_tasks, total_tasks)
            )

    # Loop through the data
    for task in data:
        # Check if the task is completed
        if task["completed"]:
            # Print the task title with a tabulation and a space before it
            print("\t {}".format(task["title"]))
else:
    # Print an error message if the response status code is not 200
    print("Error: Unable to get data from the API")
