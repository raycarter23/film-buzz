# Generated by Django 4.2.16 on 2024-12-09 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_tmdb_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='poster_url',
            new_name='poster',
        ),
    ]
