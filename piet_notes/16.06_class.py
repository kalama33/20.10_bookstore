class Parent:
    def __init__(self):
        print("Parent's constructor")
       
    def greet(self):
        print("Hello from the Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child's constructor")
       
    def greet(self):
        super().greet()
        print("Hello from the Child class")



child = Child()
child.greet()


class Animal:
    def __init__(self):
        print("Animal's constructor")

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        print("Dog's constructor")
        
class Parent:
    def __init__(self):
        print("Parent's constructor")
       
    def greet(self):
        print("Hello from the Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child's constructor")
       
    def greet(self):
        super().greet()
        print("Hello from the Child class")



child = Child()
child.greet()       