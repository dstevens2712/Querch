from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category


# Create your views here.
class Home(View):           #Get the Home page for Quotable Quotes
    def get(self, request):
        quote_form = QuoteForm()
        return render ( 
            request,
            'index.html',
            {
                'quote_form' : quote_form
            },
        )
    # # def post(self, request):
    #     form = QuoteForm(request.POST)
    #     form.save()
        # return redirect ('results')

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
        if 'save_quote' in request.POST:
            quote_form = QuoteForm(request.POST)
            quote_form.save()

class Results(View):
    def get(self, request, quote_ids):
        quotes = []
        for quote_id in quote_ids:
            quotes.append(Quote.objects.filter(id=quote_id))
            
        return render(
            request,
            template_name='results.html',
            context={
                'quotes' : quotes
            }
        )


