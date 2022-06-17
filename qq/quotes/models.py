from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# These are the quotes diplaying the relationships
class Quote(models.Model):

    text = models.TextField()
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    author = models.ForeignKey('Author', on_delete = models.CASCADE)

    def __str__(self):
        if self.text:
            return self.text        
       

# Charfield created with a default for author
class Author(models.Model):
    author = models.CharField(max_length = 250, default='Anonymous')
    
    def __str__(self):
       return self.author 

#Charfield created with a default that if there is no tag id the code will not break
class Tag(models.Model):
    tag = models.CharField(max_length = 250, null=True, blank=True)
    
    def __str__(self):
       return self.tag 

#Charfield created with a default that if there is no category id the code will not break
class Category(models.Model):
    category = models.CharField(max_length = 250, null=True, blank=True)
    
    def __str__(self):
       return self.category 


