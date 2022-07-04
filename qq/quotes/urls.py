from django.urls import path
from .views import Home, AboutUs, AddQuote, Results, Result, Update, SignUpView, Search
from .import views

# connects our code to a specific page
# code will render the following URLs: /home /about /add /results

#These paths() function define a pattern, associated generic class-based detail view, and a name.
urlpatterns = [
    path('', Home.as_view(), name='home'),
    # Path to the About view.
    path('about', AboutUs.as_view(), name='about'),
    # Path to add a quote.
    path('add', AddQuote.as_view(), name='add'),
    # Path to results.
    path('results', Results.as_view(), name='results'),
    # Path to a Result.
    path('result/<int:quote_id>', Result.as_view(), name='result'),
    # Path to the update file.
    path('update/<int:quote_id>', Update.as_view(), name='update'),
    # The path to the search page.
    path("search/", Search.as_view(), name='search'),
    # The path to the signup view
    path('signup/', SignUpView.as_view(), name='signup')
]
