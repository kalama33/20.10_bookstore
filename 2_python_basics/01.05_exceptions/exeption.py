"""
# Task 1 Exception

while True:
    try:
        num = int(input("Enter a number to divide 1:"))
        result = 1/num
        break
    except ZeroDivisionError:
        print("Error: Cannot divide by 0. Please enter a non-zero number.")

print(f"1/{num} = {result}")
        
# Task 2

while True:
    try:
        first_number = int(input("Enter your first number:"))
        second_number = int(input("Enter your second number:"))
        div = first_number/second_number
        print(f"Result of division: {div}")
    
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")
    
    except ZeroDivisionError:
       print("Error: Cannot divide by 0.")
    
    else:
        break  
    
    """
# Task 3

while True:

    try: 
        numbers = input("Give me a list of numbers:")
        num_list = numbers.split(",")
        num_list2 = []
        
        for num in num_list:
            num = int(num)
            num_list2.append(num)
        
        average = sum(num_list2)/len(num_list2)
        print(f"The average number is: {average}")
        
    except ValueError:
        print("Error: Invalid input. Please enter a list of integers, separated by commas.")
    else:
        break
        
    