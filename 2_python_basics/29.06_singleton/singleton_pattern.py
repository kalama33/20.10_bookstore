"""class Singleton:
    _instances = {}

    def __init__(self, class_):
        self._class = class_
        # self._instances = {}

    def __call__(self, *args, **kwargs):
        if self._class not in self._____:
            self._instances[_______] = _________________
        return self._instances[self._______]

@Singleton
class FirstClass:
    def __init__(self, m):
        self.val = m

a = FirstClass(1)
b = FirstClass(23)

a == b #True
research the __ call__ method
fill out the _______ spaces.
make sure that only one instance per class is created"""

class Singleton:
    _instances = {}

    def __init__(self, class_):                 # initialize variable _class, it will be wrapped by Singleton
        self._class = class_

    def __call__(self, *args, **kwargs):        # object will be called as a func.
        if self._class not in self._instances:  # Verify if the wrapped _class exists already on the dict. instances
            self._instances[self._class] = self._class(*args, **kwargs) # if not, we create a new instance from the class 
        return self._instances[self._class]

@Singleton                                      # just one instance of Firstclass
class FirstClass:
    def __init__(self, m):
        self.val = m

a = FirstClass(1)                               # Create 2 instances 
b = FirstClass(23)

print(a == b)  # True