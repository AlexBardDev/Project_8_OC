from django.contrib import admin 
from .models import Food, Category, NutritionalInformation, Bookmark

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(NutritionalInformation)
admin.site.register(Bookmark)
