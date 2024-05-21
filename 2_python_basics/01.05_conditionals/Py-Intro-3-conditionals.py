my_name = input("What's your name? ")
my_age = int(input("How old? "))  # Cast the result of input to an integer

if (my_age <= 17):
    # Check the name
    # Nested conditionals
    if (my_name == "Veera"):            # Conditional statement
        # Indentation is critical in Python!
        print("Hi Veera")
        score = 10
    elif (my_name == "Rauli"):
        # Indentation is critical in Python!
        # Indentation creates a section or sequence of code
        print("Heyyyyyy Rauli")
        score = 99
    else:
        print("Who are you even?")
        score = 3

    print("SCORE: ", score)
else:
    print("Nope. Just for kidz!")