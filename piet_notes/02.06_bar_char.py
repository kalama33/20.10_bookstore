import matplotlib.pyplot as plt

# Data
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [5000, 8000, 3000, 6000]

# Create bar chart
plt.bar(products, sales)

# Add label to axes
plt.xlabel('Products')
plt.ylabel('Sales')

# tittle
plt.title("Sale's performance")

# show it
plt.show()