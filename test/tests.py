
import builtins
import unittest
import cocktail, beer, wine, main
from unittest import TestCase
from unittest.mock import patch
import requests

class TestBeer(TestCase):

    @patch('beer.get_beer_data')
    def test_beer_api(self, mock_get_beer_data):
        mock_data = mock_get_beer_data.return_value = [{ "id": 1,"name": "Buzz",}]
        beer_call = beer.get_beer_data(1)
        self.assertEqual(mock_data, beer_call)

class TestCocktail(TestCase):

    @patch('cocktail.get_cocktail_data')
    def test_cocktail_api(self, mock_get_cocktail_data):
        mock_data = mock_get_cocktail_data.return_value = [{ "drinks": {"idDrink": "14195",
"strDrink": "Snowball"}}]
        cocktail_call = cocktail.get_cocktail_data()
        self.assertEqual(mock_data, cocktail_call)

class TestWine(TestCase):

    @patch('wine.get_wine_data')
    def test_wine_api(self, mock_get_wine_data):
        mock_data = mock_get_wine_data.retrun_value = {'pairings': ['cabernet sauvignon', 'malbec', 'shiraz'],
 'text': ' It goes especially well with cabernet sauvignon, malbec, and '
         'shiraz.'}
        wine_call = wine.get_wine_data('chicken')
        self.assertEqual(mock_data,wine_call)

class TestMain(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_first_menu_call(self):
        first_choice = main.main('1')
        self.assertEqual(1,first_choice)

    @patch('builtins.input', side_effect=['2'])
    def test_first_menu_call(self):
        secound_choice = main.main('2')
        self.assertEqual(2,secound_choice)

    @patch('builtins.input', side_effect='chicken')
    def test_search_input(self):
        food_choice = main.get_alcohol_pairings('chicken')
        self.assertTrue(food_choice)

if __name__ == '__main__':
    unittest.main() 