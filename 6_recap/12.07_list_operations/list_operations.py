numbers_list = [2, 4, 6, 7, 8, 10, 11, 15]

def list_operations(numbers):
    
    sum_of_numbers = sum(numbers) # sum of all num
    
    largest_number = max(numbers) # largest number
    
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return sum_of_numbers, largest_number, (even_count, odd_count) # tuple
   
 # Test the function

def list_operations(numbers):
    
    sum_of_numbers = sum(numbers) # sum of all num
    
    largest_number = max(numbers) # largest number
    
    even_count = len([num for num in numbers if num % 2 == 0])
    odd_count = len(numbers) - even_count

    return sum_of_numbers, largest_number, (even_count, odd_count)

result = list_operations(numbers_list)

print("Sum:", result[0])
print("Largest number:", result[1])
print("Even and odd counts:", result[2])
print(result) # tuple

"""

"""