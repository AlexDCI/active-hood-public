from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("home/", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    # Add more URL patterns as needed
]
