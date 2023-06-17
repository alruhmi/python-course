def get_min_number(data: list) -> int:
    result = None

    for number in data:
        if result is None:
            result = number
        elif number < result:
            result = number

    return result


def get_size(data: list) -> int:
    result = 0

    for number in data:
        result += 1

    return result


def greet(name: str, job: str = 'programmer'):
    print('hello ' + name)
    print('job: ' + job)
    
def sum(x, y):
    return x + y

list = [3434, 945, 534, 3324, 445, 4098, 545433]

print('min salery: ' + str(get_min_number(list)))

print(list)
# greet(name='fahmi')
# greet(name='ruqaeh', job='housewife')
# greet('mazen')
# greet('ethar')
# greet('rafat')
# print(get_size('fdfsfsfsf'))
# print(get_size([1, 4, 5, 2]))
