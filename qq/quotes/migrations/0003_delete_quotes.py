# Generated by Django 4.0.4 on 2022-05-03 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_author_category_tag_quote_meme_quote_author_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quotes',
        ),
    ]