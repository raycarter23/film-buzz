from django.db import models

# Create your models here.

class Post(models.Model):
    """
    Represents movie blog posts
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    content = models.TextField()
    intro = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=20)
    image = models.FileField(upload_to='blog')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug