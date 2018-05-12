import re

from django.shortcuts import render, redirect
from .models import Food, NutritionalInformation
from django.contrib.auth.models import User

def home(request):
    """This function returns the home of the web site."""
    
    if request.method == "POST":
        input_user = request.POST.get("research")
        return redirect("search", input_user)
    else:
        return render(request, "food_substitute/home.html")

def search(request, input_user):
    """This function searches a healthier substitute and shows the results."""

    result = Food.objects.filter(name=input_user)

    if len(result) == 0:
        list_suggestions = [food for food in Food.objects.all() if re.search(input_user, food.name)]
        if len(list_suggestions) != 0:
            context = {"product": input_user, "list_suggestions":list_suggestions}
            return render(request, "food_substitute/suggestion.html", context)
        else:
            context = {"product":input_user}
            return render(request, "food_substitute/not_found.html", context)
    else:
        result = result[0]
        list_substitute = [food for food in Food.objects.filter(id_category=result.id_category) if ord(food.nutriscore) < ord(result.nutriscore)]
        
        context = {"product":result, "list_substitute": list_substitute}

        return render(request, "food_substitute/search.html", context)

def display(request, name_product):
    """This function displays the information about a selected product."""

    
    product = Food.objects.filter(name=name_product)[0]

    context = {"product": product, "list_letters":["A", "B", "C", "D", "E"]}
    
    return render(request, "food_substitute/display.html", context)

def login(request):
    """This function allows the connexion of the users."""

    if request.method == "POST":
        #email = request.POST.get("email")
        #password = request.POST.get("password")
        pass
    else:
        return render(request, "food_substitute/login.html")
    
def create_account(request):
    """This functions creates a user account."""

    if request.method == "POST":
        pass
    else:
        return render(request, "food_substitute/account.html")

