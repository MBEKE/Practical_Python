# Command-Line Task Manager

A simple Python-based command-line application to manage tasks. This task manager allows you to create, read, update, and delete tasks while saving task information in a text file.

## Features

- **Add Task**: Create new tasks with descriptions and priority levels.
- **List Tasks**: Display all existing tasks.
- **Update Task**: Modify the description and priority of an existing task.
- **Delete Task**: Remove tasks by ID.
- **Search Tasks**: Find tasks based on keywords in the description.

## Project Structure

```plaintext
task_manager/
│
├── main.py               # Main script to run the application
├── operations.py         # Contains task-related operations (CRUD)
└── tasks.txt             # Text file for storing tasks
main.py: The main entry point for the application, providing a menu-driven interface for managing tasks.
operations.py: Contains the core functions for task management operations, including add, update, delete, list, and search tasks.
tasks.txt: A text file that stores task data in a comma-separated format: id,description,priority.
Getting Started
Prerequisites
Python 3.x installed on your machine.
Installation
Clone or download this repository.
Open a terminal and navigate to the project directory.
Usage
Run the task manager by executing  python3 main.py
Follow the prompts in the command-line interface to manage tasks:

1: Add a new task.
2: List all tasks.
3: Update an existing task by ID.
4: Delete a task by ID.
5: Search for tasks by keyword.
6: Exit the application.
Examples
Adding a Task:

plaintext
Copy code
Select an option (1-6): 1
Enter task description: Complete Python project
Enter task priority (low, medium, high): high
Output: Task "Complete Python project" added with priority "high".

Listing Tasks:

plaintext
Copy code
Select an option (1-6): 2
Output:

plaintext
Copy code
Current tasks:
ID: 1 | Description: Complete Python project | Priority: high
Edge Cases Handled
Task IDs are unique and generated based on the total number of tasks.
Invalid task IDs are checked during update and delete operations.
Incorrect input formats for task IDs and priority are validated with prompts.
Missing tasks.txt file is handled by automatically creating it when adding the first task.
Contributing
Contributions are welcome! Feel free to submit a pull request or suggest improvements.

License
This project is not licensed

vbnet
Copy code

This `README.md` provides an overview of the project's purpose, structure, usage instructions, and 
