class Point:
    default_color = 'Red'  # it's a class level attribute

    def __init__(self, x, y):
        # these are instant level attributes
        self.x = x
        self.y = y

    def drawing(self):
        print(f'Point ({self.x}, {self.y})')


# if we change class level attribute value,it is changed for all objects.
Point.default_color = 'Yellow'
point = Point(1, 2)
# calling class level attributes with the object and class name
print(point.default_color)
print(Point.default_color)
point.drawing()
another = Point(3, 4)
another.drawing()
print(another.default_color)
