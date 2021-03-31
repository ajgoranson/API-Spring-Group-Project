# Cocktail class
import sqlite3
import os

db = os.path.join('database', 'food_alcohol_pairing.db')

class Cocktail:
    def __init__(self, cocktail_api_data):
        self.cocktail_api_data = cocktail_api_data 

    def drink(self):
        return self.cocktail_api_data['drinks'][0]['strDrink'] # returns the cocktail drink extracted from the api data

    def picture(self):
        return self.cocktail_api_data['drinks'][0]['strDrinkThumb']

    def ingredients(self):
        return self.cocktail_api_data['drinks'][0]['strIngredient1'],self.cocktail_api_data['drinks'][0]['strIngredient2'], self.cocktail_api_data['drinks'][0]['strIngredient3']

    
    def instuctions(self):
        return self.cocktail_api_data['drinks'][0]['strInstructions']

class Beer:
    def __init__(self, beer_api_data):
        self.beer_api_data = beer_api_data 

    def drink(self):
        return self.beer_api_data[0]['name'] # returns the beer name extracted from the api data

class Wine:
    def __init__(self, wine_api_data):
        self.wine_api_data = wine_api_data

    def drink(self):
        return self.wine_api_data['pairings'][0] # returns the wine extracted from the api data


class Food_Alcohol:
    def __init__(self, food, cocktail, beer, wine):
        self.food = food
        self.cocktail_bev = cocktail
        self.beer_bev= beer
        self.wine_bev = wine


    # stores the food, cocktail, beer, and wine in the database 
    def save(self):       
        con = sqlite3.connect(db)
        con.execute('INSERT INTO food_alcohol (food, cocktail, beer, wine) VALUES (?, ?, ?, ?)',(self.food, self.cocktail_bev, self.beer_bev, self.wine_bev))
        con.commit()
        con.close()


    
        


