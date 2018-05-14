from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/<input_user>', views.search, name="search"),
    path('product/<name_product>', views.display, name="display"),
    path('create_account/', views.create_account, name="create_account"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('bookmarks/', views.bookmarks_user, name="bookmarks"),
    path('legal_notices/', views.legal_notices, name="legal_notices"),
    path('contact/', views.contact, name="contact"),
]
