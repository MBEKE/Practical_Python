#!/usr/bin/python3
from typing import List

FILE_NAME = "tasks.txt"

def load_tasks() -> List[str]:
    """Load task from a text file"""
    try:
        with open(FILE_NAME, 'r') as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks = []
    return [task.strip() for task in tasks]

def save_tasks(tasks: List[str]):
    """Save tasks to the text file."""
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks: List[str], description: str, priority: str = 'medium'):
    """Add a new task to the list and save it to file"""
    task_id = len(tasks) + 1
    task = f"{task_id},{description},{priority}"
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added with priority '{priority}'.")

def list_tasks(tasks: List[str]):
    """Display all tasks."""
    if not tasks:
        print("No tasks found")
    else:
        print("\nCurrent tasks:")
        for task in tasks:
            task_id, description, priority =task.split(',')
            print(f"ID: {task_id} | Description:{description} | Priority: {priority}")

def update_task(tasks: List[str], task_id: int, description: str, priority: str):
    """ Update an existing task."""
    updated = False
    for i, task in enumerate(tasks):
        tid, _, _ = task.split(',')
        if int(tid) == task_id:#.split(','):
            tasks[i] = f"{task_id},{description},{priority}"
            updated = True
            break
    if updated:
        save_tasks(tasks)
        print(f"Task ID {task_id} updated.")
    else:
        print(f"Task ID {task_id} not found.")

def delete_task(tasks: List[str], task_id: int):
    """Delete a task by its ID."""
    for i, task in enumerate(tasks):
        tid, _, _, =task.split(',')
        if int(tid) == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task ID {task_id} deleted.")
            return
    print(f"Task ID {task_id} not found")

def search_tasks(tasks: List[str], keyword: str):
    """Search tasks containing the keyword in their description"""
    results = [task for task in tasks if keyword.lower() in task.split(',')[1].lower()]
    if results:
        print("\nSearch Results")
        for task in results:
            task_id, description, priority = task.split(',')
            print(f"ID: {task_id} | Description: {description} | Priority: {priority}")
    else:
        print("No matching tasks found.")
