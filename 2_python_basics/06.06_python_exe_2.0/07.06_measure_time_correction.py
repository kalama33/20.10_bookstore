import time

# decorator for time measuring
def measure_time(func):
    def inner(list,value):
        start = time.time()
        func(list,value)
        end = time.time()
        elapsed = end - start
        return elapsed
    return inner

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

# x = range(1,1001)
x = [num for num in range(1,1001) if num % 4 == 0]
y = [binary_search (range(1, num), -1) for num in x]

import matplotlib 