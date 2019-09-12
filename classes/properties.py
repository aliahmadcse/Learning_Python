class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('Price can\'t be less than zero')
        self.__price = price


product = Product(10)
product.price = 11
print(product.price)
