#!/usr/bin/python3

import json
from sys import argv

def gather_employee_todo_progress(employee_id):
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error: Failed to retrieve TODO list for employee ID:", employee_id)
        return
    
    todos = response.json()
    employee_name = todos[0]['name'].split()[0]  # Assumes the employee name is the same for all todos
    
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos)
    
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_num_tasks))
    for task in completed_tasks:
        print("\t", task)
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py [employee_id]")
    else:
        employee_id = int(sys.argv[1])
        gather_employee_todo_progress(employee_id)
