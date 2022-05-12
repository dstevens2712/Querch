from django.contrib import admin
from django.urls import path
from .views import Home, AboutUs, AddQuote

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('about', AboutUs.as_view(), name='about'),
    #path('add', AddQuote.as_view(), name='add'),
]
