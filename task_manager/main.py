#!/usr/bin/python3

import sys
from operations import load_tasks, add_task, list_tasks, update_task, delete_task, search_tasks

def main():
    """The program's entry point"""
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")

        try:
            choice = int(input("Select an option (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number from (1-6): ")
            continue
        if choice == 1:
            description = input("Enter task description: ")
            priority = input("Enter task priority(low, medium, high): ").lower()
            add_task(tasks, description, priority)
        elif choice == 2:
            list_tasks(tasks)
        elif choice == 3:
            try:
                task_id = int(input("Enter task ID to update: "))
                description = input("Enter new description")
                priority = input("Enter new priority (low, medium, high): ").lower()
                update_task(tasks, task_id, description, priority)
            except ValueError:
                print("Invalid input for task ID.")
        elif choice == 4:
            try:
                task_id = int(input("Enter task_ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("Invalid input for task ID")
        elif choice == 5:
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)
        elif choice == 6:
            print("Exiting Task Manager")
            sys.exit()
        else:
            print("Invalid option. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main( )
        
        

