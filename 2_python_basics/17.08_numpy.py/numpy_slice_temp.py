import numpy as np

temperature_data = np.array([[28, 30, 32, 29, 27, 26, 28],
                             [31, 33, 30, 29, 28, 25, 26],
                             [24, 26, 25, 28, 30, 29, 27],
                             [22, 23, 26, 21, 20, 24, 26],
                             [29, 31, 33, 32, 30, 28, 27]])

# Slice and print the temperatures for the first 3 cities and the first 5 days.

subarray = temperature_data[0:3, 0:5] #[:3, :5]

print(subarray)


# average temperature

average_temps = np.mean(temperature_data, axis=1)

print(average_temps)


# 

