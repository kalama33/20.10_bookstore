def sum_of_digits(n):
    if n == 1: # exit condition
        return 1
    else: # recursive case
        return n + sum_of_digits(n-1)
    
print("*"*50)

# 2nd version
    
def sum_of_digits(n):
    if n == 0: # exit condition
        return n
    else: # recursive case
        return n + sum_of_digits(n-1)
    
print(sum_of_digits(10))

print("*"*50)

def sum_nested_list(nested_list):
    total_sum = 0 # initialize counter
    for element in nested_list: # loop
        if isinstance(element, list): # verifying if the element is a list
            total_sum += sum_nested_list(element) # if it is, we add it
        else:
            total_sum += element
    return total_sum

# Testing the function
nested = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
result = sum_nested_list(nested)
print(f"The sum of elements in the nested list is {result}.")

print("*"*50)

def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n-1)

countdown(5)

print("*"*50)

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)

print(power(2, 3))

