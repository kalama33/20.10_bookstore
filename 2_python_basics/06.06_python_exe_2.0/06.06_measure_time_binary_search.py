import time
import matplotlib.pyplot as plt

# define the measure_time decorator
def measure_time(func):
    def wrapper(*args, **kwargs):
        # start measuring time
        start_time = time.time()
        #execute the wrapped function
        result = func(*args, **kwargs)
        # end measuring the execution time
        end_time = time.time()
        #calculate the execution time
        execution_time = end_time - start_time
        return execution_time
    return wrapper

# define the binary search func

@measure_time
def binary_search(lst_sorted, value):
    while len(lst_sorted) > 1:
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
        
    return False

X = range(1, 1001)
X = [num for num in X if num % 4 == 0]
# initialize a list with the execution times
times = []

# Iterate over the input sizes
for size in X:
    # Create a sorted list of the specified size
    lst = list(range(size))
    # Specify a value that is not present in the list
    value = size + 1
    # Measure the execution time of binary_search function
    execution_time = binary_search(lst, value)
    # Store the execution time in the times list
    times.append(execution_time)

# Plot the input size against the execution time
plt.plot(X, times)
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Binary Search Execution Time')
plt.show()

