# lamba functions

def my_func():
    print("Hello")
    
another_name = my_func

my_func()

another_name()

lamda_func_name = lambda: print("Hello from Lamda")

lamda_func_name()

# lambda (argument)
# the power of lambda func. is that I can pass func. as arguments in a short way.

lamda_func_name_1 = lambda x :print(f"The passed arguent was {x}")

lamda_func_name_1(5)

lamda_func_name_2 = lambda x, y :print(f"The passed arguent were {x} and {y}")

lamda_func_name_2(5,10)

def higher_level_function( func_arg, x):
    func_arg, (x)
    
def my_func(x):
    print(f"The arg was {x}")
    
my_func(3)

higher_level_function(my_func, 5)
    
