from django.contrib import admin
from django.urls import path
from .views import Home, AboutUs

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('about', AboutUs.as_view, name='about'),
]

