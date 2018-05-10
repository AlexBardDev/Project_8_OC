import re

from django.shortcuts import render, redirect
from .models import Food

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

    context = {"product": product}
    
    return render(request, "food_substitute/product.html", context)
