def factorial(n):
    if n == 0: # exit condition
        return 1
    else: # recursive case
        return n * factorial(n-1)
    
print(factorial(5))

# (5 * 4 * 3 * 3 *1) = x

def factorial(n):
    result = 1 
    for i in range(1, n+1):
        result*= i
    return result

print(factorial(5))

''' Fibonacci; 

fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2), for n > 1
'''