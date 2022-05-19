from django.db import models


# Create your models here.

class Quote(models.Model):

    text = models.CharField(max_length=5000)
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    author = models.ForeignKey('Author', on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.text:
            return self.text        
       


class Author(models.Model):
    author = models.CharField(max_length = 250, default='Anonymous')
    
    def __str__(self):
       return self.author 


class Tag(models.Model):
    tag = models.CharField(max_length = 250, null=True, blank=True)
    
    def __str__(self):
       return self.tag 


class Category(models.Model):
    category = models.CharField(max_length = 250, null=True, blank=True)
    
    def __str__(self):
       return self.category 

  


  



