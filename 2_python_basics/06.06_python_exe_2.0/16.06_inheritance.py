import math

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# create instances of rectangle and circle
rectangle = Rectangle("Rectangle", 5, 10)
circle = Circle("Circle", 3)

# add shapes to a list
shapes = [rectangle, circle]

# calculate and print the total area
total = total_area(shapes)
print("Total Area:", total)
