from django.contrib import admin
from django.db import models

# Register your models here.
class Quotes(models.Model):
    text = models.CharField(max_length = 3000)
    '''
    meme = models.ImageField(upload_to)#need to complete this code
    pass
'''