import requests


def fetch_product_data(product_id):
    #  API 
    api_url = f"https://fakestoreapi.com/products/{product_id}"
    
    # send get request
    response = requests.get(api_url)
    
    # check  status code is 200 (OK)????
    if response.status_code == 200: # succesfull response
        product_data = response.json() #json format
        #print(type(product_data))
        return product_data
    else:
        print("Error: Failed to fetch.")
        return None

def main():
    try:
        # promp product id
        product_id = int(input("Enter product ID: "))
        
        # fetch p data, we call the previous func
        product_data = fetch_product_data(product_id)
        
        if product_data:
            # product info
            print("Product Name:", product_data["title"])
            print("Product Category:", product_data["category"])
            print("Product Price:", product_data["price"])
            print("Product Description:", product_data["description"])
    except ValueError: # handle error
            print("Error: Invalid input. Please enter a valid product ID.")

if __name__ == "__main__":
    main()



