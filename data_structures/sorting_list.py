numbers = [3, 45, 2, 7, 12, 66]

# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
# print(numbers)

items = [('product1', 12), ('product2', 3), ('product3', 10)]


def sort_item(item):
    return item[1]


items.sort(key=sort_item,reverse=True)
print(items)