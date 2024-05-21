# Task 1

print("Welcome to the guessing number game")

print()

import random

sec_num = random.randint(1, 100000)
user_num = 0 #
num_of_guesses = 0 #

while user_num != sec_num:
    user_num = int(input("Guess the number between 1 and 100000: "))
    num_of_guesses += 1 #
    
    print("-------------------")
    
    if user_num == sec_num:
       print("You guessed the secret number.")
       print("It took you", num_of_guesses, "guesses.")
    
    if user_num < sec_num:
       print("Oops, your number is lower than the secret number" )
       print("-------------------")
       print("Please try again.")
       print("-------------------")
    
    if user_num > sec_num: 
       print("Oops, your number is higher than the secret number" )
       print("-------------------")
       print("Please try again.")
       print("-------------------")







    
    






