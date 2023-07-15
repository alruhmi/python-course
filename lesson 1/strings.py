name = 'fahmi'
age = 29

template = f"----My name is {name.capitalize()} and I'm {age} years old.\\".rstrip('\\').lstrip('-')

print(template.find('fahmi'))
print(template.endswith('.'))
print(template.startswith("I'm"))
print(template.lower())
print(template.upper())
print(name.isupper())
print(template.replace('Fahmi', 'Shehab'))