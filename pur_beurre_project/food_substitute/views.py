from django.shortcuts import render, redirect
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

    result = Food.objects.filter(name=input_user)[0]

    context = {"product":result}

    return render(request, "food_substitute/search.html", context)

