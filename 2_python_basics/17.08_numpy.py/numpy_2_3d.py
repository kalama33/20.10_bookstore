import numpy as np

# Generate consecutive odd numbers starting from 1
odd_numbers = np.arange(1, 2 * 3 * 2 + 1, 2)

# Reshape the array to have shape (2, 3, 2)
odd_array_3d = odd_numbers.reshape(2, 3, 2)

print(odd_array_3d)