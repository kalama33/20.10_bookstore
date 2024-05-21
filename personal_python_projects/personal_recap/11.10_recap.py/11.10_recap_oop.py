
# 1 create class 

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
# create student, inheritance

class Student(Person):
    def __init__(self, first_name, last_name, student_id): # new atribute
        super().__init__(first_name, last_name)
        self.student_id = student_id
        
    def get_details(self):
        return f"Student Id: {self.student_id}, Name: {self.full_name()}"
    
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width =width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        def __init