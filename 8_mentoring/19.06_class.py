class MyClass:
    pass
print(type(MyClass))

object_1 = MyClass()

MyClass

print(type(object_1))

class Dog:
    def __init__(self, breed,name,age):
        self.breed = breed
        self.name = name
        self.age = age
        
    def increase_age(self):
        self.age += 1
        
my_dog = Dog("Greyhound", "Mapple", 2)

your_dog = Dog("Labrador", "Roco", 3)

print(my_dog.name)
print(your_dog.name)

print(my_dog.age)
print(your_dog.age)

my_dog.increase_age()

# encapsulation
# inheritance
# 

