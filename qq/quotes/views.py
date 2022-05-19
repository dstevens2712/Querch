from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
import random
from django.http.response import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class Home(View):          
    def get(self, request):
        num = Quote.objects.count()
        quote_id = random.randrange(1, num)
        daily = Quote.objects.get(id = quote_id)
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
            'add_quote.html',
            {
                'quote_form' : quote_form,
            }
        )

    def post(self, request):
        print(request.POST)
        if 'save_quote' in request.POST:
            quote_form = QuoteForm(request.POST)
            if quote_form.is_valid():
               quote_form.save()
            # return HttpResponseRedirect(reverse('result', kwargs = {'quote_id' : Quote.objects.latest('pk').pk}
            return redirect('home')
            
            

            
class Results(View):
   
    def get(self, request):
        category = request.GET['category']
        if category:
            obj = Category.objects.get(category = category)
            quotes = Quote.objects.filter(category = obj.id)

        return render(
            request,
            template_name='results.html',
            context={
                'quotes' : quotes
            }
        )

class Result(View):
    def get(self, request, quote_id):
        quote = Quote.objects.get(id = quote_id)
        quote_form = QuoteForm(instance = quote)   
        return render(
            request,
            template_name='result_detail.html',
            context={
                'quote' : quote,
                'quote_form' : quote_form
            }
        )
    
    def post(self, request, quote_id):
        '''Update or delete a quote'''
        quote = Quote.objects.filter(id = quote_id)
        if 'save' in request.POST:
            form = QuoteForm(request.POST)
            if form.is_valid():
                quote_description = form.cleaned_data['text']
                author = form.cleaned_data['author']
                quote.update(text = quote_description, author = author)
            return redirect('result')

        elif 'delete' in request.POST:
            quote.delete()

            return redirect('home')
        

       




# class Import(View):
#     def author():
#             path = ('quotes.csv')
#             with open(path) as f:
#                 reader = csv.reader(f)
#             for row in reader:
#                 _, created = Author.objects.get_or_create(
#                 author = row[1] if row[1] else 'Anonymous'
#                 )
#             created.save()

#     def quote():
#             path = Path('quotes.csv').resolve()
#             with open(path) as f:
#                 reader = csv.reader(f)
#             for row in reader:
#                 a = Author.objects.get(author = row [1])
#                 _, created = Quote.objects.get_or_create(
#                 text = row[0],
#                 author = a.id
#                 )
#             created.save()


