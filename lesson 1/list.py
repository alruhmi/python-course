users = ['fahmi', 'ahmed', 'sad']

print(users[2])

users[2] = 'rafat'

print(users)

users.append('mazen')

print(users)

print(len(users))

users.extend(['shehab', 'abdullah'])

print(users)

print(users.index('shehab'))

users.insert(2, 'salem')

print(users)

name = users.pop()

print(name)
print(users)

print('rafat' in users)

if 'rafat' in users:
    users.remove('rafat')

print(users)

users.sort(reverse=True)

print(users)
