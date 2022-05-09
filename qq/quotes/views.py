from django.shortcuts import render, redirect
from django.views import View
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
# Create your views here.
class Home(View):
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


class Results(View):
    def get(self, request):
        return render(request, 'results')

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
    def get(self, request, quote_id, author_id):
    
        quote_object = Quote.objects.get(id=quote_id)
        quote_form = QuoteForm(quote=quote_object)
 
        authors = quote_object.author.all()
        author_form = AuthorForm(author=author_object)
        return render(
            request,
            template_name='results.html',
            context={
                'quote_form':quote_form,
                'id':quote_id,
                'author_form':author_form,
            }
        )

