from django.shortcuts import render

def home(request):
    """This is the home of the web site"""

    return render(request, "food_substitute/home.html")


