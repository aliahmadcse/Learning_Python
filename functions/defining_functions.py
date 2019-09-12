def greet(name):
    return f'Hi {name}'


if __name__ == '__main__':
    message = greet('Ali Ahmad')
    file = open('4-functions/file.txt', 'w')
    file.write(message)
