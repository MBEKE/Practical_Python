#!/usr/bin/python3

# List to store tasks
tasks = []

def add_task():
    """
    Prompts the user to input a task and adds it to the task list.
    """
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f'Task "{task}" has been added to the list')

def list_tasks():
    """
    Lists all tasks in the task list.
    If there are no tasks, informs the user that the list is empty.
    """
    if not tasks:
        print('There are no tasks currently.')
    else:
        print('Here are the tasks:')
        for idx, task in enumerate(tasks):
            print(f'{idx}. {task}')  # Shows task index for easier deletion reference

def delete_task():
    """
    Prompts the user to enter the index of the task to delete.
    If a valid index is given, removes the task from the task list.
    Handles invalid input gracefully.
    """
    list_tasks()  # Show current tasks for user reference

    try:
        task_to_delete = int(input('Enter the # of the task to delete: '))
        
        # Check if the input index is within the valid range
        if 0 <= task_to_delete < len(tasks):
            removed_task = tasks.pop(task_to_delete)
            print(f'Task "{removed_task}" has been removed')
        else:
            print('Invalid task number.')
    except ValueError:
        print('Invalid input. Please enter a task number.')
