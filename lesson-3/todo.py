import json

file = open('todos.json', 'r+')

todos: list = json.load(file)

index = 1

print('№ | task               |  complated')

todo: dict
for todo in todos:
    print(index, todo.get('task') + '       ', todo.get('complated'), sep=' | ')
    index += 1


command = input('choose command to do with todos (create, complate, delete, edit): ')

if command == 'create':
    task = input("Enter your task: ")
    todos.append({
        'task': task,
        "complated": False
    })
elif command == 'complate':
    i = int(input('Enter task №: '))
    todos[i-1]['complated'] = True
elif command == 'delete':
    i = int(input('Enter task №: '))
    todos.pop(i-1)
elif command == 'edit':
    i = int(input('Enter task №: '))
    task = input("Enter your task: ")
    todos[i-1]['task'] = task
    
    
index = 1

print('№ | task               |  complated')

todo: dict
for todo in todos:
    print(index, todo.get('task') + '       ', todo.get('complated'), sep=' | ')
    index += 1

file.seek(0)

file.truncate()

json.dump(todos, file, indent=4)

file.close()