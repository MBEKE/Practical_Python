#1/usr/bin/python3
tasks = []

def add_task():
    task = input("Please enter a task; ")
    tasks.append(task)
    print(f'Task "{task}" has been added to the list')


def list_tasks():
    if not tasks:
        print('There are no tasks currently.')
    else:
        print('Here are the tasks:')
        for task in tasks:
            print(f'- {task}')
def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input('Enter the #  to delete: '))
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f'Task #{task_to_delete} has been removed')
    except:
        print('Invalid input.')