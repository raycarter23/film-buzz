# Generated by Django 4.2.16 on 2024-12-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default='', upload_to='blog'),
            preserve_default=False,
        ),
    ]
