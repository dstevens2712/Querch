from django.contrib import admin
from django.urls import path
from .views import Home, AboutUs, AddQuote, Results, Result

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('about', AboutUs.as_view(), name='about'),
    path('add', AddQuote.as_view(), name='add'),
    path('results', Results.as_view(), name='results'),
    path('result/<str:quote_id>', Result.as_view(), name='result'),
]
