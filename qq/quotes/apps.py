from django.apps import AppConfig

# Here we create a quotes config class for our App
class QuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotes'
