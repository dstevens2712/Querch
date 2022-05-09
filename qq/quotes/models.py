from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 250)
     
class Quote(models.Model):
<<<<<<< HEAD
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
=======
    text = models.CharField(max_length=1000)
    # meme = models.ImageField(upload_to='images', default='')
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    author = models.ForeignKey('Author', on_delete = models.CASCADE, default='Anonymous', null=True, blank=True)


    def __str__(self):
        if self.text:
            return self.text        
        # return self.meme


class Author(models.Model):
    author = models.CharField(max_length = 250)
    
    def __str__(self):
       return self.author 
>>>>>>> b906e2bf424e8687ff295a1c43bdc2fd15c4d4cc




'''
class Tag(models.Model):
    tag = models.CharField(max_length = 250)
    
    def __str__(self):
       return self.tag 
<<<<<<< HEAD
pass
'''
=======

class Category(models.Model):
    name = models.CharField(max_length = 250)
    
    def __str__(self):
       return self.name 

  


  



>>>>>>> b906e2bf424e8687ff295a1c43bdc2fd15c4d4cc
