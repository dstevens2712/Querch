from django.db import models



# Create your models here.


class Quote(models.Model):
    text = models.CharField(max_length=1000)
    meme = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.text


class Author(models.Model):
    author = models.CharField(max_length=1000)
   
    def __str__(self):
        return self.author


class Tag(models.Model):
    Tag = models.CharField(max_length=1000)
   
    def __str__(self):
        return self.Tag


class Category(models.Model):
    category = models.CharField(max_length=1000)
   
    def __str__(self):
        return self.category


class Quote_Tag(models.Model):
    manufacturer = models.ForeignKey(
        'Quote',
        on_delete=models.CASCADE,
    )


class Category_Quote(models.Model):
    manufacturer = models.ForeignKey(
        'Quote',
        on_delete=models.CASCADE,
    )
