items = [('product-1', 12), ("product-2", 10), ('product-3', 15)]

items.sort(key=lambda item: item[1])

print(items)
