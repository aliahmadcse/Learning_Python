numbers = [1, 2, 3, 4, 2, 5, 6, 6]
first = set(numbers)
second = {1, 2, 7}

print(first | second)
print(first & second)
print(first-second)
print(first ^ second)  # items that are either in first or second set but not both
if 1 in first:
    print('yes')