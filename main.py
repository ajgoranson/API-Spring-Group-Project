# This program selects the best alcoholic drink that goes with your food
from sqlite3.dbapi2 import Cursor
import cocktail, beer, wine
from alcohol import *
import os
import sqlite3


db = os.path.join('database', 'food_alcohol_pairing.db')

def main():
    while True:
        try:
            menu() # prints the menu
            selection = int(input('Select from the Menu:  '))

            if selection == 1:
                get_alcohol_pairings()
            elif selection == 2:
                show_pairings()
            elif selection == 3:
                delete_recent_data()
            else:
                quit()
        except Exception as e:
            print(e)

def menu():
    print ('\n Menu: \n'
    '1: Find a cocktail, beer, and wine for your food\n'
    '2: Display your recent saves \n'
    '3: Delete saved data\n'
    'Any other number to quit\n')


def save_selection(food, cocktail, beer, wine):
    food_alcohol = Food_Alcohol(food, cocktail, beer, wine)
    food_alcohol.save()

def show_pairings():
    """ returns entire database """

    try:

        get_all_pairings = 'SELECT food, * FROM food_alcohol'

        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        rows = con.execute(get_all_pairings)
        

        if rows is None:
            print('Sorry looks like you havent saved any food pairings yet. Try again after you save some data')
        else:
            for r in rows:
                print(f"\nFor {r['food']}, the following drinks are suggested:\n"
                f"Cocktail: {r['cocktail']}\n"
                f"Beer: {r['beer']}\n"
                f"Wine: {r['wine']}\n")

    except Exception as e:
        print('There was an error finding your saved data, try saving some data then looking first' + e)

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
                
    save = input('Would you like to save this drink selection?? press Y to save, otherwise hit enter to continue: ').upper()
    if save == 'Y':
        save_selection(food, cocktail_drink, beer_drink, wine_drink) # saves the food, cocktail, beer, wine into the database

    picture = input('Would you like to view a picture of the drink in your web browsers?? press Y to view otherwise hit enter to continue: ').upper()
    if picture == 'Y':
        show_picture()
    else:
        main()

    

def delete_recent_data():

    delete_data = 'DELETE FROM food_alcohol'

    try:
        with sqlite3.connect(db) as conn:
            conn.execute(delete_data)
        conn.close()
    except Exception as e:
        print('There was an error deleting data, try saving some data first' + e)

def show_picture():

    cocktaildata = cocktail.get_cocktail_data()
    cocktailpicutre = cocktaildata.picture()
    print(f'Here is the url for your picutre simply copy and paste into your browser for your picture: {cocktailpicutre}')

    instructions_ingredients = input('Does this drink look incredibly tasty??? Would you like to know how to make it? Press Y or hit enter to contiune: ').upper()

    if instructions_ingredients == 'Y':
        show_instructions()
    main()


def show_instructions():
    cocktaildata = cocktail.get_cocktail_data()
    cocktail_instructions = cocktaildata.instuctions()
    cocktail_ingredients = cocktaildata.ingredients()


    print(f'Here are the ingredients you will need! {cocktail_ingredients} To make the cockail here is the instructions \n {cocktail_instructions}')
    main()



if __name__ == '__main__':
    main()
