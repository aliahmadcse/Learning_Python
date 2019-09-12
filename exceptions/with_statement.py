try:
    with open('with_statement.py') as file:
        print('file opened')
except FileNotFoundError as ex:
    print(ex)
finally:
    print('I am final clause')
