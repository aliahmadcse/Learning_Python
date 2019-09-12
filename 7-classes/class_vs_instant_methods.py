class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #a decorator for defining a class method, it's a way to extend the
    # behaviour of a method or function
    @classmethod
    def zero(cls):
        return cls(0,0)

    # this is an instant level method
    def drawing(self):
        print(f'Point ({self.x}, {self.y})')


point = Point.zero()
point.drawing()


