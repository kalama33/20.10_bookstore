"""
Scope referes to the region of a program ewhere a particular variable is accesicle.

1. locals
2. global

"""
# global scope

x = 10

def print_global():
    print(x)
    
print_global()

"""
Local Scope:

- A variable defines inside a func is said to be in the local scope.
-Local variables can only be accessed from within the function in which they are defined.    

"""
# local scope 

y = 5 
def print_local():
    print(y)
    
print_local()
#print(y)

# Global vs local

z = 10 

def print_global_vs_local():
    z = 5
    print(z)
    
print_global_vs_local()
print(z)

# Global 