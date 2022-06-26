from django.contrib import admin
from .models import Quote, Tag, Category, Author


# Registering our site
 
admin.site.register(Quote)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)

