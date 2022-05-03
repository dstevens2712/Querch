from django.db import models



# Create your models here.


class Quote(models.Model):
    text = models.CharField(max_length=1000)
    meme = models.ImageField(upload_to='images', default='')
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    author = models.ForeignKey('Author', on_delete = models.CASCADE, default='')


    def __str__(self):
        if self.text:
            return self.text        
        return self.meme


class Author(models.Model):
    author = models.CharField(max_length=1000)
   
    def __str__(self):
        return self.author


class Tag(models.Model):
    tag = models.CharField(max_length=1000)
   
    def __str__(self):
        return self.tag


class Category(models.Model):
    category = models.CharField(max_length=1000)
   
    def __str__(self):
        return self.category


