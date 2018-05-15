import re

from django.shortcuts import render, redirect
from .models import Food, NutritionalInformation, Bookmark
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(request):
    """This view returns the home of the web site."""
    
    if request.method == "POST":
        input_user = request.POST.get("research")
        return redirect("search", input_user)
    else:
        return render(request, "food_substitute/home.html")

def search(request, input_user):
    """This view searches a healthier substitute and shows the results."""

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
        paginator = Paginator(list_substitute, 6)
        page = request.GET.get('page')
        list_page_substitute = paginator.get_page(page)
        context = {"product":result, "list_substitute": list_page_substitute}

        return render(request, "food_substitute/search.html", context)

def display(request, name_product):
    """This view displays the information about a selected product."""

    
    product = Food.objects.filter(name=name_product)[0]

    context = {"product": product, "list_letters":["A", "B", "C", "D", "E"]}
    
    return render(request, "food_substitute/display.html", context)

def login_user(request):
    """This view allows the connexion of the users."""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect("home")
    else:
        return render(request, "food_substitute/login.html")
    
def create_account(request):
    """This view creates a user account."""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        new_user = User.objects.create_user(email, email, password)
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
        return redirect("home")
    else:
        return render(request, "food_substitute/account.html")

def logout_user(request):
    """This view logs out a user."""

    logout(request)

    return redirect("home")

@login_required
def bookmark_user(request):
    """This view returns all the saved substitutes of the user."""

    list_bookmarks = Bookmark.objects.filter(id_user=request.user.id)

    context = {"list_bookmarks": list_bookmarks}

    return render(request, "food_substitute/bookmark.html", context)

@login_required
def save_product(request, name_product):
    """This view saves a new bookmark for the current user."""

    product = Food.objects.filter(name=name_product)[0]
    user = request.user

    Bookmark.objects.create(id_user=user, id_product=product)

    return redirect("home")

def legal_notices(request):
    """This view returns the legal notices page."""

    return render(request, "food_substitute/legal_notices.html")

