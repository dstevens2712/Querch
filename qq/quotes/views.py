from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
from random import choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
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
       
            

class AboutUs(View):
    def get(self, request):
        return render(request, 'about.html')

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

    def post(self, request):
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            author = Author.objects.get(author = quote_form.cleaned_data['author'])
            quote = Quote.objects.create(text = quote_form.cleaned_data['text'], author = author) 
            quote.tags.set(quote_form.cleaned_data['tags'])
            quote.category.set(quote_form.cleaned_data['category']) 
            quote.save()
        
        return redirect('result', quote.id)
            
class Results(View):
   
    def get(self, request):
        category = request.GET['category']
        if category:
            obj = Category.objects.get(category = category)
            quotes = Quote.objects.filter(category = obj.id)

        return render(
            request,
            'results.html',
            context={
                'quotes' : quotes,
                'category' : category
            }
        )

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
            
                return redirect('result', quote.id)                        
            
            
            quote.delete()

            return redirect('home')

                     


        
  
       
