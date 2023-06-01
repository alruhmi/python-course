users_count = 4

users = []

while users_count > 0:
    name = input("Enter user name: ")
    phone = input("Enter user phone: ")
    email = input("Enter user email: ")
    age = input("Enter user age: ")
    
    user = {
        "name": name,
        "phone": phone,
        "email": email,
        "age": age,
    }
    
    users.append(user)
    
    users_count = users_count - 1

for user in users:
    print("user name: " + user.get("name"))
    print("user email: " + user.get("email"))
    print("user phone: " + user.get("phone"))
    print("user age: " + user.get("age"))
    print("--------------------------------------", "\n")
