import random
import timeit
import matplotlib.pyplot as plt

def quicksort_second_pivot(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[1]
        less = [num for i, num in enumerate(lst) if num <= pivot and i != 1]
        greater = [num for i, num in enumerate(lst) if num > pivot and i != 1]

    return quicksort_second_pivot(less) + [pivot] + quicksort_second_pivot(greater)

def quicksort_random_pivot(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot_index = random.randint(0, len(lst) - 1)
        pivot = lst[pivot_index]
        less = [num for i, num in enumerate(lst) if num <= pivot and i != pivot_index]
        greater = [num for i, num in enumerate(lst) if num > pivot and i != pivot_index]

    return quicksort_random_pivot(less) + [pivot] + quicksort_random_pivot(greater)

# Generate input list X
X = range(1, 1001)
X = [num for num in X if num % 4 == 0]

array_sizes = list(X)

execution_times_second_pivot = []
execution_times_random_pivot = []

for size in array_sizes:
    array = [random.randint(0, 1000) for _ in range(size)]
    
    # Measure execution time for quicksort with second pivot
    time_second_pivot = timeit.timeit(lambda: quicksort_second_pivot(array.copy()), number=1)
    execution_times_second_pivot.append(time_second_pivot)
    
    # Measure execution time for quicksort with random pivot
    time_random_pivot = timeit.timeit(lambda: quicksort_random_pivot(array.copy()), number=1)
    execution_times_random_pivot.append(time_random_pivot)

# Plotting the results
plt.plot(array_sizes, execution_times_second_pivot, label='Quicksort with Second Pivot')
plt.plot(array_sizes, execution_times_random_pivot, label='Quicksort with Random Pivot')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()
