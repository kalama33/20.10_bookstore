import matplotlib.pyplot as plt

y = [100000, 110000, 120000, 130000, 140000]
x = [2018, 2019, 2020, 2021, 2022]

plt.plot(x, y)

plt.scatter(2018, 100000, color='red', label='Point')
plt.scatter(2019, 110000, color='red', label='Point')
plt.scatter(2020, 120000, color='red', label='Point')
plt.scatter(2021, 130000, color='red', label='Point')
plt.scatter(2022, 140000, color='red', label='Point')

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population growth')
plt.show()