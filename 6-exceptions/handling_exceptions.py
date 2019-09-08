try:
    age = int(input('Age : '))
    xFactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid value")
else:
    print('No exception')

print('Execution Continues')
