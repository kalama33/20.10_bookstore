import requests

# URL de tu API
url = 'http://127.0.0.1:8000/api/products/'

# Realizar una solicitud GET
response = requests.get(url)
print("GET Response:", response.json())

# Datos para una solicitud POST
product_data = {'name': 'Nuevo Producto', 'price': 10.99}

# Realizar una solicitud POST
post_response = requests.post(url, data=product_data)
print("POST Response:", post_response.json())
