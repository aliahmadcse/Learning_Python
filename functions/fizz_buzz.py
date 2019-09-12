def fizz_buzz(input):
    if input % 3 == 0 and input % 3 == 0:
        return 'Fizz Buzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'buzz'
    return input


print(fizz_buzz(15))
