from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/<input_user>', views.search, name="search"),
    path('product/<name_product>', views.display, name="display"),
]
