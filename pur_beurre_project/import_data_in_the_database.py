#External library
import requests
import django
import math
from django.db import transaction

#Standard library
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pur_beurre_project.settings')
django.setup()

#Local library
from food_substitute.models import Food, NutritionalInformation, Category

#Some constants
URL_ALL_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"
URL_CATEGORY = "https://fr.openfoodfacts.org/categorie/{}/{}.json"

categories = requests.get(URL_ALL_CATEGORIES).json()["tags"]
for i in range(100):
    #Save a category
    name_category = categories[i]["url"].split("/")[-1]
    if len(Category.objects.filter(name=name_category)) == 0:
        new_category = Category.objects.create(name=name_category)
        print("""{} saved.""".format(name_category))

    #Save food
    for k in range(1,4):
        try:
            data = requests.get(URL_CATEGORY.format(name_category, k)).json()["products"]
        except:
            print("""HTTP request doesn't work. Category = {} and k = {}""".format(name_category, k))
            break
        else:
            for product in data:
                try:
                    name = product["product_name_fr"]
                except:
                    continue
                else:
                    if len(Food.objects.filter(name=name)) == 0:
                        try:
                            #Food
                            nutriscore = product["nutrition_grades"]
                            image = product["image_url"]
                            link = product["url"]

                            #Nutritional information
                            nutritional_data = product["nutriments"]

                            calories = math.ceil(int(nutritional_data["energy_100g"])*0.239006)
                            fat = int(nutritional_data["fat_100g"])
                            saturated_fat = int(nutritional_data["saturated-fat_100g"])
                            carbohydrates = int(nutritional_data["carbohydrates_100g"])
                            sugars = int(nutritional_data["sugars_100g"])
                            proteins = int(nutritional_data["proteins_100g"])
                            salt = int(nutritional_data["salt_100g"])
                            sodium = int(nutritional_data["sodium_100g"])

                            with transaction.atomic():
                                #Save nutritional information
                                new_row = NutritionalInformation.objects.create(calories=calories,
                                        fat=fat, saturated_fat=saturated_fat, carbohydrates=carbohydrates, sugars=sugars,
                                        proteins=proteins, salt=salt, sodium=sodium)

                                #Save food
                                new_food = Food.objects.create(name=name, id_category= new_category,
                                        nutriscore=nutriscore, id_nutritional_information= new_row,
                                        image=image, link=link)
                                print("""{} saved""".format(name))
                        except:
                            continue

