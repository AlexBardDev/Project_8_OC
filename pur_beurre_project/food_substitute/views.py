from django.shortcuts import render, redirect

def home(request):
    """This function returns the home of the web site"""
    
    if request.method == "POST":
        input_user = request.POST.get("research")
        return redirect("search", input_user)
    else:
        return render(request, "food_substitute/home.html")

def search(request, input_user):
    """This function searches a healthier substitute and shows the results."""

    data = {"clé1": input_user}

    return render(request, "food_substitute/search.html", data)

