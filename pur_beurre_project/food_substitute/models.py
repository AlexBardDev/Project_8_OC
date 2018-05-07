from django.db import models

# Create your models here.

class Category(models.Model):
    """This class is the 'Category' table in the database. It stores all the
    categories."""

    name = models.CharField(max_length=50)

class NutritionalInformation(models.Model):
    """This class is the 'NutritionalInformation' table in the database. It
    stores all the nutritional information for 100g."""

    calories = models.PositiveSmallIntegerField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    carbohydrates = models.FloatField()
    sugars = models.FloatField()
    proteins = models.FloatField()
    salt = models.FloatField()
    sodium = models.FloatField()

class Food(models.Model):
    """This class is the 'Food' table in the database. It stores all the
    information about food."""

    name = models.CharField(max_length=50)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutriscore = models.CharField(max_length=1)
    id_nutritional_information = models.ForeignKey(NutritionalInformation, on_delete=models.CASCADE)
    image = models.URLField()
    link = models.URLField()

class User(models.Model):
    """This is the 'User' table in the database. It stores all the information
    about the users."""

    pass

class Bookmarks(models.Model):
    """This class is a join table called 'Bookmarks' in the database. It stores
    which user has saved which food."""

    pass
