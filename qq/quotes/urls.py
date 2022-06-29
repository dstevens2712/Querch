from django.urls import path
<<<<<<< HEAD
from .views import Home, AboutUs, AddQuote, Results, Result, Update, Search
=======
from .views import Home, AboutUs, AddQuote, Results, Result, Update
from .import views
>>>>>>> 9cfc2959ebd49f8dde7c3e963423c496f8d45b16

# connects our code to a specific page
# code will render the following URLs: /home /about /add /results


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', AboutUs.as_view(), name='about'),
    path('add', AddQuote.as_view(), name='add'),
    path('results', Results.as_view(), name='results'),
    path('result/<int:quote_id>', Result.as_view(), name='result'),
    path('update/<int:quote_id>', Update.as_view(), name='update'),
<<<<<<< HEAD
    path("search/", Search.as_view(), name='search')
=======
    # path('quote/'. quote_list.as_view, name='quote_list'),
>>>>>>> 9cfc2959ebd49f8dde7c3e963423c496f8d45b16
]

