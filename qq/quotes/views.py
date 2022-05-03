from django.shortcuts import render
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
]

def index(request):
    pass

# Create your views here.
