from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster = models.URLField(blank=True, null=True) # URL for movie poster
    tmdb_id = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Optional: TMDb ID for API integration

    def __str__(self):
        return self.title