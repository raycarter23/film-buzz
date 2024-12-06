from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True) # URL for movie poster
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)  # Optional: TMDb ID for API integration

    def __str__(self):
        return self.title