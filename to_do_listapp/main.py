#!/usr/bin/python3
from tasks import add_task, delete_task, list_tasks # type: ignore
'''
This module runs the To Do List App
'''
if __name__ == '__main__':
    # Create a loop to run the app
    print('welcome to the to do list app :)')
    while True:
        print('\nPlease select one of the following options')
        print('-----------------------------------------')
        print('1: Add new task')
        print('2: Delete a task')
        print('3: List tasks')
        print('4: Quit')

        # Collect user input
        choice = input("Enter your Choice: ")

        if(choice == '1'):
            add_task()
        elif(choice == '2'):
            delete_task()
        elif(choice == '3'):
            list_tasks()
        elif(choice == '4'):
            break
        else:
            print('Invalid input ❌. Please try again')
        
    print('Goodbye 👋')