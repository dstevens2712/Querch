<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-05-09 23:55
=======
# Generated by Django 4.0.4 on 2022-05-10 22:57
>>>>>>> fd373922cf63fcd85b14fce19a99d90d62230532

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(blank=True, default='Anonymous', null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.author')),
                ('category', models.ManyToManyField(to='quotes.category')),
<<<<<<< HEAD
=======
                ('tags', models.ManyToManyField(to='quotes.tag')),
>>>>>>> fd373922cf63fcd85b14fce19a99d90d62230532
            ],
        ),
    ]
