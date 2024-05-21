import pandas as pd

airbnb_data = pd.read_csv("28.08_pandas/data/listings_austin.csv")


# listings with minimum stay requirement
long_stay_listings = airbnb_data[airbnb_data['minimum_nights'] >= 7]

# average price for both groups
avg_price_long_stay = long_stay_listings['price'].mean()
avg_price_non_long_stay = airbnb_data[airbnb_data['minimum_nights'] < 7]['price'].mean()

print("Average price for long stay listings:", avg_price_long_stay)
print("Average price for non-long stay listings:", avg_price_non_long_stay)