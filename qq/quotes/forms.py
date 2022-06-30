from django import forms
from .models import Quote, Author, Category, Tag, User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here
# For user input (create, read, update, delete)
# Model form for the Quote class with fields that include text, author, category, and tags
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'category', 'tags']

# Function to init Class. Inheriting arguments and key word arguments
# Creating an instance of the Author class and then assigns values to the fields text
    def __init__(self, *args, **kwargs):
        authors = Author.objects.all()
        super().__init__(*args, **kwargs)
        self.fields['text'].label = 'Quote'
        self.fields['author'].label = 'Author'
        self.fields['category'].label = 'Category'
        self.fields['tags'].label = 'Tags'


 # Creates a form that allows users to select a category  
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
#  Model that represents the form with two fields: Tag which is an interger tied to the ID of tag in our database, and Quote while is an interger is tied to our text of a quote. We also use some methods that will save, create, update, and delete objects in our database
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
    
    def __init__(self, *args, **kwargs):
        self.quote = kwargs.pop('quote', None)
        super().__init__(*args, **kwargs)

        self.instance.quote = self.quote
        self.fields['tag'].label = 'Tag'

    def save(self, *args, **kwargs):

        tag, create = Tag.objects.get_or_create(tag=self.data['tag'])
        self.quote.tags.add(tag)


# class RegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=100)
#    # password = forms.CharField()
#     #email = forms.CharField()
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ["username", "password1", "password2", "email"]


        
