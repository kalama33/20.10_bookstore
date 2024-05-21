import pandas as pd

airbnb_data = pd.read_csv("28.08_pandas/data/listings_austin.csv")

price_by_neighborhood = airbnb_data.groupby(['neighbourhood', 'room_type'])['price'].mean()

print(price_by_neighborhood)