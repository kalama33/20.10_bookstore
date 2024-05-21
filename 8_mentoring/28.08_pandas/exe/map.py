import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

airbnb_data = pd.read_csv("28.08_pandas/data/listings_austin.csv")

# Group by latitude and longitude, calculate mean price
price_by_location = airbnb_data.groupby(['latitude', 'longitude'])['price'].mean().reset_index()

# Create a scatter plot with color-coded prices
plt.figure(figsize=(10, 8))
plt.scatter(price_by_location['longitude'], price_by_location['latitude'], c=price_by_location['price'], cmap='YlOrRd', s=50, alpha=0.5)
plt.colorbar(label='Mean Price')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Mean Price Distribution Map')
plt.show()
