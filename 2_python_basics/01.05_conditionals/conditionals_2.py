import random

lucky = random.randint(0,5) # Chaos!
print(lucky)

password = input("Welcome to casino Py! What can I call you? ")

if password != "Swordfish": # != is a negation, if Not True
    print("Access denied")

else: 
    if lucky == 5:
        print("Jackpot! Noice!")
    elif lucky >= 3:
        print("Pretty good")
    elif lucky == 0:
        print("Oof")
    else:
        print("Better luck next time")