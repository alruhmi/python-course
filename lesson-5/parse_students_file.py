import json

file = open("students.txt", "r")
user = None
result = {}
class_name = ""
for line in file:
    line = line.strip('\n')

    if line.endswith(':'):
        class_name = line.replace(':', '')

        result[class_name] = []

    elif line.startswith('  -'):
        if user is not None:
            result[class_name].append(user)
            user = None

        line = line.removeprefix('  - ')
        data = line.split(": ")
        user = {data[0]: data[1]}
        
    elif line.startswith('    '):
        line = line.strip()
        data = line.split(": ")
        user[data[0]] = data[1]
        
    elif line == '' and user is not None:
        result[class_name].append(user)
        user = None

file.close()

file = open('class.json', 'w+')

json.dump(result, file, indent=4)

file.close()
