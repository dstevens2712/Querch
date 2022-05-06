from django.shortcuts import render
from django.views import View

from quotes.forms import SearchForm, NavForm
from quotes.models import Home, About_us, Results
# Create your views here.
class Home(View):           #Get the Home page for Quotable Quotes
    def get(self, request):
        search_form = SearchForm  #Used to seardh database for Quotes
        nav_form = NavForm        #Used on each page for quickly finding Quote using a tag or comment
        
        return render (request = request,
        template_name = 'index.html',
        context={
            #if needed ???
        },
        )

class About_us(View):
    def get(self, request):
        nav_from = NavForm

        return render(request, template_name = 'about')
  

class Results(View):
    def get(self, request):
        nav_form = NavForm
    
        return render(request, template_name = 'results')


class Add_Quote(View):
    def get(self, request):
        pass


class Advance_search(View):
    pass


class Result(View):
    pass


