# This program selects the best alcoholic drink that goes with your food
import cocktail, beer, wine
from alcohol import Cocktail, Food_Alcohol, Beer, Wine
import os
import sqlite3

db = os.path.join('database', 'food_alcohol_pairing.db')

def main():
    while True:
        try:
            banner()
            menu() # prints the menu
            selection = int(input('Select from the Menu:  '))

            if selection == 1:
                get_alcohol_pairings()
            elif selection == 2:
                show_pairings()
            elif selection == 3:
                delete_recent_data()
            elif selection == 4:
                exit()
            else:
                quit()
        except Exception as e:
            print(e)

def menu():
    print ('Menu: \n'
    '1: Find a cocktail, beer, and wine for your food\n'
    '2: Display your recent saves \n'
    '3: Delete saved data\n'
    'Any other number to quit\n')

def banner():
    print('\nPair an alcoholic beverage with your food\n')

def save_selection(food, cocktail, beer, wine):
    food_alcohol = Food_Alcohol(food, cocktail, beer, wine)
    food_alcohol.save()

def show_pairings():
    """ returns entire database """

    get_all_pairings = 'SELECT food, * FROM food_alcohol'

    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    rows = con.execute(get_all_pairings)

    print('\nFor each food, the following drinks are suggested')
    for r in rows:
        print(f"\nFor {r['food']}, the following drinks are suggested:\n"
        f"Cocktail: {r['cocktail']}\n"
        f"Beer: {r['beer']}\n"
        f"Wine: {r['wine']}\n")

def get_alcohol_pairings():
    food = input('Enter the food: ')  #user is prompted to enter a food
    # cocktail
    cocktail_data = cocktail.get_cocktail_data() # gets the cocktail api data
    cocktail_drink = cocktail_data.drink()

    #beer
    beer_data = beer.get_beer_data() # gets the beer api data
    beer_drink = beer_data.drink()

    #wine
    wine_data = wine.get_wine_data(food) # gets the wine api data
    wine_drink = wine_data.drink()

    print(f'Here is types of alcohol that would go good with your {food}\n'
    + f'Cocktail: {cocktail_drink}\n'
    + f'Beer: {beer_drink}\n'
    + f'Wine: {wine_drink}\n')
                
    save = input('Would you like to save this drink selection?? y or n: ')
    if save == 'y':
        save_selection(food, cocktail_drink, beer_drink, wine_drink) # saves the food, cocktail, beer, wine into the database
    else:
        main()

def delete_recent_data():

    delete_data = 'DELETE FROM food_alcohol'

    con = sqlite3.connect(db)
    con.execute(delete_data)





if __name__ == '__main__':
    main()
