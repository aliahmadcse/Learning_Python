from sys import getsizeof

# number = []

# print({item:item*2 for item in range(5)})

number=(x for x in range(1000))
print(getsizeof(number))
for x in number:
    print(x)