import requests

def fetch_product_data():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return[]
    
products = fetch_product_data()

#