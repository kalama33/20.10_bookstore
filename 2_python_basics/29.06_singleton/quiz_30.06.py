class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 == s2)

class MyClass:
    def __new__(cls):
        print("Creating instance...")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing instance...")

obj = MyClass()

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            return None

animal = AnimalFactory.create_animal("dog", "Buddy")
print(animal.speak())