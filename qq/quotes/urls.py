from django.urls import path

from .views import Home, AboutUs, AddQuote, Results, Result, Update, Search

from .views import Home, AboutUs, AddQuote, Results, Result, Update, SignUpView
from .import views


# connects our code to a specific page
# code will render the following URLs: /home /about /add /results


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', AboutUs.as_view(), name='about'),
    path('add', AddQuote.as_view(), name='add'),
    path('results', Results.as_view(), name='results'),
    path('result/<int:quote_id>', Result.as_view(), name='result'),
    path('update/<int:quote_id>', Update.as_view(), name='update'),
    path("search/", Search.as_view(), name='search'),
    path('signup/', SignUpView.as_view(), name='signup')
     
]



