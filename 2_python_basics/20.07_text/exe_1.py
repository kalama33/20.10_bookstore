# Write a Python program that opens a file called "sample.txt" and prints its contents.

with open('sample.txt', 'r') as file:
    data = file.read()
    print(data)
    
# Write a Python program that opens a file called "numbers.txt", reads two integers from the file, 
# and prints their sum.
# Assume that the file "numbers.txt" contains two integers separated by a space, e.g., "10 20".

with open('numbers.txt', 'r') as file:
    numbers = file.readline().split()
    num1, num2 = int(numbers[0]), int(numbers[1])
    result = num1 + num2
    print(result)
    
with open('numbers.txt', 'r') as file:
    num1, num2 = file.read().split()
    print(int(num1) + int(num2))
    
# Write a Python program that creates a new file called "output.txt" 
# and writes the numbers 1 to 10, each on a new line.

list = []

with open('output.txt', 'w') as file:
    for i in range(1, 11):
        file.write(str(i) + '\n') #file.write(f"{num}\n")
        file.writelines(list)
        
#Write a Python program that reads the content of a file called "input.txt" and 
#writes the reversed content to a new file called "reversed.txt".

with open('input.txt', 'r') as input_file:
    content = input_file.read()

reversed_content = content[::-1]

with open('reversed.txt', 'w') as output_file:
    output_file.write(reversed_content)
    
    

# Write a Python program that reads a JSON file called "data.json" 
# and converts its contents into a dictionary.
# The "data.json" file contains information about employees in a company.
# Each employee has a name, age, and department.

import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

print(data)

employees = data["employees"]

for employee in employees:
    print("Name:", employee["name"])
    print("Age:", employee["age"])
    print("Department:", employee["department"])
    print("--------------")