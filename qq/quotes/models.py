from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 1000)
     
class Quote(models.Model):
    text = models.TextField()
    category = models.ManyToManyField('Category')
    #meme = models.ImageField(upload_to='images', default='')
    #tags = models.ManyToManyField('Tag')
'''
    def __str__(self):
        if self.text:
            return self.text        
        return self.meme
'''


class Author(models.Model):
    author = models.CharField(max_length = 500)
    quote = models.ForeignKey(Quote, on_delete = models.CASCADE, default='Anonymous', null=True, blank=True)




'''
class Tag(models.Model):
    tag = models.CharField(max_length = 1000)
    
    def _str_(self):
       return self.tag 
pass
'''
