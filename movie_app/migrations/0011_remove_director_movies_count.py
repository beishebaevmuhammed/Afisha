# Generated by Django 4.2.10 on 2024-02-24 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_director_movies_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movies_count',
        ),
    ]
