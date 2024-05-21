import pandas as pd

airbnb_data = pd.read_csv("28.08_pandas/data/listings_austin.csv")

#print(airbnb_data.head())

#print(airbnb_data.info())

#print(airbnb_data.describe())

price = airbnb_data['price']

#print(price)

price_neig = airbnb_data[['price','neighbourhood']]

#print(price_neig)

mean_price_by_hood = airbnb_data.groupby('neighbourhood')['price'].mean()

print(mean_price_by_hood)

max_price_index = airbnb_data['price'].idxmax()

max_price_hood = airbnb_data.loc[max_price_index, 'neighbourhood']

print("Most expensive hood is", max_price_hood)