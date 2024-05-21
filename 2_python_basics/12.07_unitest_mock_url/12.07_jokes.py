import requests
def get_joke():
    
    url = "https://api.chucknorris.io/jokes/random"
    
    response = request.get(url)
    
    if response.status_code == 200:
        joke = response.json()["value"]
    else:
        joke = "No jokes available"
        
    return joke    
    