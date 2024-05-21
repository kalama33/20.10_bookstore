import numpy as np

# 1D NumPy array containing integers from 0 to 9.

# array_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array_1d = np.arange(10)

print(array_1d)

# Create a 2D NumPy array with shape (3, 4) filled with random floating-point numbers between 0 and 1.

array_2d = np.random.rand(3, 4) #3 rows, 4 columns

print(array_2d)

# Create a 3D NumPy array with shape (2, 3, 2) containing consecutive odd numbers starting from 1.

odd_numbers = np.arange(1, 3, 5)

odd_array_3d = odd_numbers.reshape(2, 3, 2)

print(odd_array_3d)