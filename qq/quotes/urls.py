from django.urls import path
from quotes.views import Result, Results, AddQuote, Home, AboutUs
# from .views import Home, AboutUs, AddQuote, ResultDetailView, ResultsList, ResultDetail, ResultsListView
# from django.shortcuts import render, redirect
# from django.views import View
# from quotes.models import Quote, Tag, Category, Author
# from quotes.forms import QuoteForm

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('about', AboutUs.as_view(), name='about'),
    path('add', AddQuote.as_view(), name='add'),
    path('results', Results.as_view(), name='resultslist'),
    path('resultdetail/<int:quote_id>', Result.as_view(), name='resultdetail'),
]
