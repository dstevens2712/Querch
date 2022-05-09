<<<<<<< HEAD
from django import forms
from . models import Quote,Category, Author


=======
from asyncio import Task
from unicodedata import category
from django import forms
from .models import Quote, Author, Category, Tag 


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)
        self.fields['text'].label = 'Quote'
        self.fields['author'].label = 'Author'
        self.instance.author = self.author

    def save(self, *args, **kwargs):
        author, create = Author.objects.get_or_create(author=self.data['author'])
        self.quote.author.add(author)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.quote = kwargs.pop('quote', None)
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Category'
        self.instance.category = self.category

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
        
>>>>>>> b906e2bf424e8687ff295a1c43bdc2fd15c4d4cc
