letters = ['a', 'b', 'c', 'd']

letters.append('e')  # append at the last
letters.insert(0, '-')  # insert at any index
letters.pop()  # remove last item
letters.pop(0)  # remove at a given index
letters.remove('b')  # remove by searching an item
del letters[0:2]  # delete a range of object
letters.clear()  # clear all the list
print(letters)
