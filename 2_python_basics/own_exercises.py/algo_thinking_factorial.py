# Calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num_2 = 8
result_2 = factorial(num_2)
print(f"The factorial of {num_2} is {result_2}")

# define max number

def find_max(numbers):
    if len(numbers) == 0:
        return None  # Si la lista está vacía, no hay máximo

    max_num = numbers[0]  # Asignar el primer elemento como máximo inicial

    for num in numbers:
        if num > max_num:
            max_num = num  # Actualizar el máximo si se encuentra un número mayor

    return max_num

list = [154, 245, 367, 456]
max_num = find_max(list)
print(f"The max number of the {list} is {max_num}") # variable max_num es local

import math

def calculate_area_circle(radio):
    return math.pi * radio**2

def calculate_volume_circle(radio, height):
    base_area = calculate_area_circle(radio) # calling the other function
    volume = base_area * height
    return volume

radio = 3
height = 5
volume = calculate_volume_circle(radio, height)
print(f"the volume of the cilinder is: {volume}")

# verify even or odd

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
num = 345

if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
