# Generated by Django 4.2.16 on 2024-12-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('action', 'Action'), ('sci-fi', 'Sci-Fi'), ('romance', 'Romance'), ('drama', 'Drama'), ('thriller', 'Thriller'), ('horror', 'Horror'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('biopic', 'Biopic'), ('documentary', 'Documentary'), ('family', 'Family')], max_length=30),
        ),
    ]