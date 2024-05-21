# What about properties when subclassing?

# 1. getters and setters. No need for special treatments - just inherited func.

# 2. To define again the properties - repeat of code but clear and straight forward. " Decorator"

# 3 To use the definition of the property at the super class. Kind of special syntax.

# super class
class A():
    def __init__(self):
        self._x = 100
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, v):
        self._x = v

#subclass
class B1(A): # inheritade everything
    pass

#This is another subclass - calls the superclass properties


class B2(A):
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, v):
        self._x = v +1
        
    b1 = B1()
    
    print(b1.x) 
    
    b1.x = 2  
    
    b1 = B1()
    
    print(b1.x) 
    
    

