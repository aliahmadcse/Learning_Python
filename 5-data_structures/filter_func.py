items = [('product-1', 12), ("product-2", 10), ('product-3', 8)]

price=list(filter(lambda item:item[1]>=10,items))
print(price)