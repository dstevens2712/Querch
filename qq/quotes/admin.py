from django.contrib import admin
from .models import Quote, Tag, Category, Author

# Registering our site
 
 # Registers all the fields in the site. (Quote, Tag, Category, and Author)
admin.site.register(Quote)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
