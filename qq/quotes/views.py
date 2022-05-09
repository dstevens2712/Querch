from django.shortcuts import render, redirect
from django.views import View
<<<<<<< HEAD
from django.forms import Form
from quotes.forms import SearchForm, NavBar
from quotes.models import Home, About_us, Results
from . forms import QuoteForm 
=======
from .forms import QuoteForm, TagForm, CategoryForm
from .models import Quote, Author, Tag, Category
>>>>>>> b906e2bf424e8687ff295a1c43bdc2fd15c4d4cc
# Create your views here.
class Home(View):           #Get the Home page for Quotable Quotes
    def get(self, request):
<<<<<<< HEAD
        search_form = SearchForm  #Used to seardh database for Quotes
         
        return render (request = request,
        template_name = 'index.html',
        context={
            'search_form' : search_form
                        #if needed ???
        },
        )

    def post(self, request):
        form = SearchForm(request.POST)
        form.save()

        return redirect('results')


'''
class AboutUs(View):
    def get(self, request):

        return render(request, template_name = 'about')
''' #Do we need this class?????



class AddQuote(View):
    def get(self, request):
        quote_form =QuoteForm()

        return render( 
            request=request,
            template_name='add_quote.html',
            context={
                'quote_form' : quote_form,
                'id' : quote_id,
            }
        )       
    def post(self, request, quote_id):
        quote = Quote.objects.get(id=quote_id)

        if 'save_quote' in request.POST:
            quote_form = QuoteForm()
            quote_form.save()

        elif 'delete_quote' in request.POST:
            author.delete()

        elif 'save_author' in request.POST:
            # The user clicked the button to add a comment, not update the quote
            author_form = AuthorForm(request.POST, author=author)
            author_form.save()


class Results(View):
    def get(self, request, quote_id, author_id):
    


        quote_object = Quote.objects.get(id=quote_id)
        quote_form = QuoteForm(quote=quote_object)
#Do we nead an instance ??????????????????????????????????????
        authors = quote_object.authors.all()
        author_form = AuthorForm(author=author_object)  # Tag.objects.filter(task=task)
        
       
        return render(
        request=request,
        template_name='results.html',
        context={
            'quote_form': quote_form,
            'id': quote_id,
            'author_form': author_form,
        }
    )





class Advance_search(View):
    pass



=======
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
>>>>>>> b906e2bf424e8687ff295a1c43bdc2fd15c4d4cc

