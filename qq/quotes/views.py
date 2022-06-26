from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
from random import choice
from django.http import HttpResponse

# Create your views here.
# Pks are quote ids pulling from data base and use render to connect to the indext.html file with lists of quotes
class Home(View):          
    def get(self, request):
        pks = Quote.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        daily = Quote.objects.get(pk=random_pk)
        categories = Category.objects.all()
        
        return render ( 
            request,
            'index.html',
            {
                'daily' : daily,
                'categories' : categories
            },
        )

# data will display according to the post
# Post is taking in an argument
    def post(self, request):
        if 'category' in request.POST:
            category = request.POST['category'].lowercase()
            return render(
                request,
                'results.html',
                context={
                    'category' : category
                    }
            )


# Code of info about the creators of Quotable Quotes, showing our page on app linking to our template about.html
class AboutUs(View):
    def get(self, request):
        return render(request, 'about.html')

# this code allows a user to add a quote to our data base
class AddQuote(View):
    def get(self, request):
        quote_form = QuoteForm()
        return render(
            request,
            'quote.html',
            {
                'quote_form' : quote_form,
            }
        )

