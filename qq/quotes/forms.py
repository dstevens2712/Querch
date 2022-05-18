from asyncio import Task
from unicodedata import category
from django import forms
from .models import Quote, Author, Category, Tag 


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = 'Quote'
        self.fields['author'].label = 'Author'
        

    def save(self, *args, **kwargs):
        author, create = Author.objects.get_or_create(author=self.data['author'])
        self.instance.author = author
        super().save(*args, **kwargs)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      

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
        
