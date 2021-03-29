import requests
from alcohol import Cocktail

def get_cocktail_data():
    try:
        url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
        cocktail_data = requests.get(url).json()
        return Cocktail(cocktail_data)  # stores the cocktail api data in a cocktail class
        
    except Exception as e:
        print('Could not connect please try again', e)

