items = [('product-1', 12), ("product-2", 10), ('product-3', 8)]

price = [item[1] for item in items]
# print(price)
fil = [item for item in items if item[1] >= 10]
print(fil)
#list comprehension is a great feature
