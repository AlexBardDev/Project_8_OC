import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pur_beurre_project.settings')
django.setup()

#External library
import requests

#Standard library

#Local library
from models import Food, NutritionalInformation, Category

#Some constants
URL_ALL_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"
URL_CATEGORY = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
URL_FOOD = "https://fr.openfoodfacts.org/api/v0/produit/{}.json"

def import_data():
    """This function imports all the needed data in the database."""

    categories = requests.get(URL_ALL_CATEGORIES).json()["tags"]
    for i in range(100):
        name = categories[i]["url"].split("/")[-1]
        print(name)
