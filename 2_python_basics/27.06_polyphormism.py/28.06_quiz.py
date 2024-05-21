class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def area(self):
        return self.length * self.width

circle = Circle()
circle.radius = 5

rectangle = Rectangle()
rectangle.length = 10
rectangle.width = 7

print(circle.area())
print(rectangle.area())
