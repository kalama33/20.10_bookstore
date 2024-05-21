
#My first function!

#Here we define a function
def lucky_number():
    print("Feeling lucky?")
    print(777)
    
#Here we call that function
lucky_number()
lucky_number()

print()

def greet(name):
    print("Hello", name, "!!")
    
greet("Veera")
greet("Rauli")

print()

def triple(num):
    return num*3 #operator

result = triple(9)
print(result)

my_test = triple("Hello")
print(my_test)

print()

import random

money = 100

def double_or_nothing(bet):
    lucky = random.randint(0,1)
    if lucky == 1:
       return bet * 2 
    else:
        return -bet
    
money = money + double_or_nothing(20)
print(money)
    

    




