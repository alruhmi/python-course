import json

def print_tasks(tasks: list):
    index = 1

    print('№ | task               |  complated')

    task: dict
    for task in tasks:
        print(index, task.get('task') + '       ', task.get('complated'), sep=' | ')
        index += 1

def get_command():
    return input('choose command to do with todos (create, complate, delete, edit): ')
def create_task(tasks: list):
    task = input("Enter your task: ")
    tasks.append({
        'task': task,
        "complated": False
    })

def complate_taske(tasks: list):
    i = int(input('Enter task №: '))
    tasks[i-1]['complated'] = True

def delete_task(tasks: list):
    i = int(input('Enter task №: '))
    tasks.pop(i-1)

def edit_task(tasks: list):
    i = int(input('Enter task №: '))
    task = input("Enter your task: ")
    tasks[i-1]['task'] = task

def process_tasks(tasks: list):
    command = get_command()
    
    if command == 'create':
        create_task(tasks)
    elif command == 'complate':
        complate_taske(tasks)
    elif command == 'delete':
        delete_task(tasks)
    elif command == 'edit':
        edit_task(tasks)

file = open('todos.json', 'r+')

todos: list = json.load(file)

print_tasks(todos)

process_tasks(todos)

print_tasks(todos)

file.seek(0)

file.truncate()

json.dump(todos, file, indent=4)

file.close()