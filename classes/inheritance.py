class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def walk(self):
        print('walk')


class Fish(Animal):
    def swin(self):
        print('swim')


m = Mammal()
print(isinstance(m,object))
print(issubclass(Mammal,Animal))