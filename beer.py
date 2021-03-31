import requests
from alcohol import Beer
from random import randrange

def get_beer_data():
    try:
        randomint = randrange(325)
        url = f'https://api.punkapi.com/v2/beers/{randomint}'
        beer_data = requests.get(url).json()
        return Beer(beer_data) # stores the beer api data in a beer class

    except Exception as e:
        print('Could not connect please try again', e)

