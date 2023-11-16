# Task 1 Theoretical Warm Up

"""
1. Detecting and handling errors in a program, providing mechanism for error handling and recovery and allowing cleanup and resource management when errors occur.
2. It will propagate up the call stack until it reaches the default exception handler. This result in the program's termination and an error message being displayed.
3. Use exception hadnling techniques such as the "try-except"
4. It is used to enclose a block of code that may raise exceptions. It allows you to handel exceptions and define a behaviour to be executed in case of specific exception types
5. "try-except" and "try_finally", the first allows you to catch and handle specific excep., the second, it allows you to define cleanup code that will be executed regardless an exception is raised or not.
6. It allows you to explicitly generate except. in your code when certain conditions or errors occur.
"""

# Task 2

#1. Type your answer below (pick the correct line).

a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError:
    result = "You can't divide by 0"

print(result)

#2. Type your answer below.

a="Hello World!"
try:
    a + 10
except Exception:
    msg="You can't add int to string"
    
print(msg)
    
#3. Type your answer below.

lst=[5, 10, 20]

try:
    print(lst[5])
except IndexError:
    msg="You're out of list range" 

print(msg)



