### @property

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
#When you use the @property decorator, 
#you define a method as a property of the class
#This method can be accessed like
#an attribute of an object


rect = Rectangle(1,2)

print(rect.width)