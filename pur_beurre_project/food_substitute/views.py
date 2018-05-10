from django.shortcuts import render, redirect, get_object_or_404
from .models import Food

def home(request):
    """This function returns the home of the web site"""
    
    if request.method == "POST":
        input_user = request.POST.get("research")
        return redirect("search", input_user)
    else:
        return render(request, "food_substitute/home.html")

def search(request, input_user):
    """This function searches a healthier substitute and shows the results."""

    result = Food.objects.filter(name=input_user)

    if len(result) == 0:
        context = {"product":input_user}
        return render(request, "food_substitute/not_found.html", context)
    else:
        result = result[0]
        list_substitute = []
        list_same_catgeory = Food.objects.filter(id_category=result.id_category)
        for food in list_same_catgeory:
            if ord(food.nutriscore) < ord(result.nutriscore):
                list_substitute.append(food)

        context = {"product":result, "list_substitute": list_substitute}

        return render(request, "food_substitute/search.html", context)

