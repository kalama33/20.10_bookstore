print("---Variables---")

# Here we declare the variable amounts of cats

amount_of_cats = 2
print(amount_of_cats)


amount_of_cats = amount_of_cats + 1
print(amount_of_cats)

print(amount_of_cats + 99)
print(type(amount_of_cats))

print("---Dynamite---")
print()

spam = "eggs"
print(spam,type(spam))

spam = 42
print(spam,type(spam))

print()
print()
print()
print()

count = 1
print(count +1)
#print(count + "spam")

print(count + 1.7)
print(count + .3)
print(type(count + 7.))
print(count + True)

print("eggs" + "spam") # concatenation

print()
print()
print()
print()
print()

score = 10
print(score - 51)
print(score * 4)
print(score / 4)
print(score % 1)
print(score % 2)
print(score % 3)
print(score % 4)
print(score % 5)
print(score % 6)
print(score % 7)
print(score % 8)
print(score % 9)
print(score % 10)

print("--Exponential--")
print(score**2)
print(score**3)
print(score**4)

print("--Floor division--")
print(score // 1)
print(score // 2) #Divide and round the result down
print(score // 3)
print(score // 4)

print("---Assigment operators---")
print()
print()
print()
print()
print()
print()

score = 100
#score = score + 20
score += 30
score -= 3
print(score)

my_name = "Batman"
my_name += " Spam"
print(my_name)

print()
print()
print("---MATH FUN")
print()
print()

print(max(2, 1, 4, 9, 1))
print(min(2, 1, 4, 9, 1))
print(abs(-41)) # "absolute" value
print(pow(3,4)) # "3 to the power 4"

print(round(3.14159))
print(round(3.9))

print("")

import math

#Instead of round
print(math.ceil(1.1)) #Rounding up
print(math.ceil(1.2)) 
print(math.ceil(1.8)) 
print(math.ceil(1.9)) 
 
print("")
 
print(math.floor(1.9)) 
print(math.floor(1.9)) 
print(math.floor(1.9)) 

my_name = input("What is your name? ")
print("Hello", my_name)
print(type(my_name))

print("")

money = input("How much you got? ")
money = float(money) #Cast the money STRING value to a number It will not recognize a Integer
money = money * 3
print("Now you have", money)