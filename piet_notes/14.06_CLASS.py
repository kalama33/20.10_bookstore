class Dog:
    def __init__(self, name, breed, is_real_dog=True): # constructor: is used to initialize the attributes
        print('address self:', self)
                                    #of the object
        self.name = name
        self.breed = breed
        if is_real_dog:
            self.legs = 4
        else:
            self.legs = 8

    # self is a reference to the object being created
    # name and breed are attributes
    
    def bark(self):
    # The _bark_ method is a function
    # can be called on an object of the Dog class to make it bark
        print(self.name)
        print('Woof!')

dog_obj = Dog('goofy', 'australian dog', True)
print('adress dog_obj: ', dog_obj)