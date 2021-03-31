import requests
from alcohol import Wine

def get_wine_data(order):
    url= 'https://api.spoonacular.com/food/wine/dishes'
    
    # See slack for the API key
    key = '9306bd5b9f7442a99ef6a19bb1b56319'
    wine='%s'%(order)
    params = {'wine': wine, 'apiKey': key}
    wine_data = requests.get(url, params).json()

    return Wine(wine_data) # stores the wine api data in a wine class