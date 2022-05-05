from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        
        return render (request = request, template_name = 'index.html')


class About_us(View):
    def get(self, request):

        return render(request, template_name = 'about')


class Results(View):
    def get(self, request):

        return render(request, template_name = 'results')     