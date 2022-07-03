from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
from random import choice
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
# Pks are quote ids pulling from data base and use render to connect to the indext.html file with lists of quotes
class Home(View):
    def get(self, request):
        pks = Quote.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        daily = Quote.objects.get(pk=random_pk)
        categories = Category.objects.all().order_by('category')
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
            'registration.html',
            {
                'quote_form' : quote_form,
            }
        )
# define variables for form, after user edits it returns clean data
    def post(self, request):
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            author = Author.objects.get(author = quote_form.cleaned_data['author'])
            quote = Quote.objects.create(text = quote_form.cleaned_data['text'], author = author)
            quote.tags.set(quote_form.cleaned_data['tags'])
            quote.category.set(quote_form.cleaned_data['category'])
            quote.save()
        return redirect('result', quote.id)
# Results page with all quotes displayed according to category
class Results(View):
      def get(self, request):
        category = None
        try:
            category = request.GET['category']
        except:
            pass
        if category:
            obj = Category.objects.get(category = category)
            quotes = Quote.objects.filter(category = obj.id)
            context={
                'quotes': quotes,
                'category': category,
                'all': False
                }
        else:
            categories = Category.objects.all().order_by('category')
            quotes = []
            for single_category in categories:
                category_quotes = Quote.objects.filter(category = single_category.id)
                quotes.append(category_quotes)
            all_quotes = zip(categories, quotes)
            context = {
            'all_quotes': all_quotes,
            'all' : True
            }
        return render(
            request,
            'results.html',
            context
        )
# This page displays a selected quote for further editing
class Result(View):
    def get(self, request, quote_id):
        quote = Quote.objects.get(id = quote_id)
        return render(
            request,
            'result_detail.html',
            context={
                'quote' : quote,
            }
        )
# Here the user edits(update) the quote and can delete the quote
class Update(View):
    def get(self, request, quote_id):
        quote = Quote.objects.get(id = quote_id)
        quote_form = QuoteForm(instance = quote)
        return render(
                    request,
                    'quote.html',
                    context={
                       'quote' : quote,
                       'quote_form' :  quote_form
                    }
                )
    def post(self,  request, quote_id):
        quote = Quote.objects.get(pk = quote_id) # this is the quote as in the db
        quote_form = QuoteForm(request.POST)  # this is the updated data
        if quote_form.is_valid():
            if 'update' in request.POST: # updating the db
                quote.text = quote_form.cleaned_data['text']
                author = Author.objects.get(author = quote_form.cleaned_data['author'])
                quote.author = author
                quote.tags.set(quote_form.cleaned_data['tags'])
                quote.category.set(quote_form.cleaned_data['category'])
                quote.save()
                return redirect('result', quote.id) # Here you will be directed back to the result page page                      
            quote.delete()
            return redirect('home') # If deleted a quote you will be directed back to home page
class Search(View):
    def get(self, request):
        try:
            search = request.GET['quote']
            quote = Quote.objects.filter(
               text__icontains=str(search))
            authors = Author.objects.filter(author__icontains=str(search))
            author_quotes = Quote.objects.filter( author__in=authors)
            context = {
                "search": search,
                "quotes": quote,
                "authors": authors,
                "author_quotes":author_quotes
            }

            return render(request, "search.html", context)

        except Exception as e:
            print(e) 

            return render(request, "search.html")

                     
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

