from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    """
    Represents a movie category
    """
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('sci-fi', 'Sci-Fi'),
        ('romance', 'Romance'),
        ('drama', 'Drama'),
        ('thriller', 'Thriller'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('crime', 'Crime'),
        ('biopic', 'Biopic'),
        ('documentary', 'Documentary'),
        ('family', 'Family')
    ]
    title = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    slug = models.SlugField()

    def __str__(self):
        return self.get_title_display()
    
    def get_absolute_url(self):
        return f"/{self.slug}"

class Post(models.Model):
    """
    Represents movie blog posts
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/blog')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug

class Comment(models.Model):
    """
    Represents a comment made on a movie blog post
    """
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'Comment from {self.user} on {self.post}'


