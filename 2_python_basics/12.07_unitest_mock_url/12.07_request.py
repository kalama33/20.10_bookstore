import requests

url = "https://fakestoreapi.com"

response = requests.get(f"{url}/products")

#print(response.json()[5])

print(response.raw.read())