from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
from random import choice
from django.http import HttpResponse

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
            'add_quote.html',
            {
                'quote_form' : quote_form,
            }
        )

    def post(self, request):
        print(request.POST)
        if 'create' in request.POST:
            quote_form = QuoteForm(request.POST)
            if quote_form.is_valid():
                author, _ = Author.objects.get_or_create(author = quote_form.cleaned_data['author'])
                print(author)
                quote_form = quote_form.save()
            
            return redirect('add')
            
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
                'quotes' : quotes
            }
        )

class Result(View):
    def get(self, request, quote_id):
        quote = Quote.objects.get(id = quote_id)
        quote_form = QuoteForm(instance = quote)   
        
        return render(
            request,
            'result_detail.html',
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
                author = Author.objects.get_or_create(id = form.cleaned_data['author'])
                quote.update(text = quote_description, author = author)
            return redirect('results')

        elif 'delete' in request.POST:
            quote.delete()

            return redirect('home')





#class Search(View):
 #   def Search(request):
  #      if request.method == "POST":
   #         author_name = request.POST.get('name', None)
        # if author_name:
        #     results = Search.objects.filter(name__contains=author_name)
        #     return render(request, 'search.html', {"results":results})

        # return render(request, 'search.html')
     




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


