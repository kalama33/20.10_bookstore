print("---Variables---")

# Here we declare the variable amount_of_cats
# We also assign it the value 2
amount_of_cats = 2
print(amount_of_cats)

# Here we are reusing the same variable
# We reassign it the value 2 + 1
amount_of_cats = amount_of_cats + 1
print(amount_of_cats)

# Let's experiment
print(amount_of_cats + 99)
print(type(amount_of_cats))

print("---Dynamite---")
print()

# A string? Nice
spam = "eggs"
print(spam, type(spam))

spam = 42
print(spam, type(spam))

print()
print()
print("---OPERATORS---")
print()
print()

count = 1
print(count + 1)
print(type(count + 1))
# print(count + "spam")

# Hmmm... decimals and ints are both numbers
print(count + 1.7) # Like I said; depending on the type
print(count + .3)
print(type(count + 7.))
print(count + True) # Like I said; depending on the type

print("eggs" + "spam" + "spam" + "cherry")


print()
print()
print("---Operators---")
print()
print()

score = 10
print(score - 51)
print(score * 4)
print(score / 4)
print("----")
print(score % 1) # Modulus / Modulo / Remainder / Residual
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
print(score ** 2)
print(score ** 3)
print(score ** 4)

print("--Floor division--")
print(score // 1)
print(score // 2)
print(score // 3) # Divide and round the result down
print(score // 4)
print(score // 5)
print(score // 6)
print(score // 7)

print()
print()
print()
print()
print("---Assignment operators---")
print()

score = 100
# score = score + 20   The old way
score += 30 # Same as above, except with 30 instead of 20
score -= 3
print(score)

my_name = "Batman"
my_name += " Spam"
print(my_name)




print()
print()
print("----MATH FUN----")
print()
print()

print(max(2, 1, 4, 9, 1, 9))
print(min(2, 1, 4, 9, 1, 9, 0.1, -3))
print(abs(5))
print(abs(-41)) # "absolute", distance from 0
print(pow(3,4)) # "3 To the power of 4"
print(round(3.14159))
print(round(3.9))
print(round(3.499999999,4))
print(round(13.12345678,4))

import math

# Instead of round
print(math.ceil(1.1)) # Rounding, but... always up!
print(math.ceil(1.2)) # Rounding, but... always up!
print(math.ceil(1.8)) # Rounding, but... always up!
print(math.ceil(1.9)) # Rounding, but... always up!
print(math.floor(1.1)) # Rounding, but... always down!
print(math.floor(1.2)) # Rounding, but... always down!
print(math.floor(1.8)) # Rounding, but... always down!
print(math.floor(1.9)) # Rounding, but... always down!


print()
print()
print()
print()
print()
print()
print()

my_name = input("Whats your name traveller? ")
print("Hello", my_name)
print(type(my_name))

print()
print()
print()
print()
print()
print()

money = input("How much you got? ")
money = float(money) # Cast the money STRING value to a float
money = money * 3
print("Now you have", money)
