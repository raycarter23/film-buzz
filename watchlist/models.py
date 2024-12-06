from django.db import models
from django.conf import settings
# from movies.models import Movie

# Create your models here.

# class Watchlist(models.Model):
#     """
#     Represents a user's custom watchlist of movies
#     """
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='watchlists'
#     )
    
#     movie_title = models.CharField(max_length=255)  # Title of the movie
#     movie_id = models.IntegerField()  # TMDb movie ID for API integration
#     movie_image = models.URLField(blank=True, null=True)  # URL for the movie's poster image
#     note = models.TextField(blank=True, null=True)  # User notes for the movie
#     created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when added to the watchlist
#     slug = models.SlugField(unique=True, blank=True, null=True)  # Optional unique slug for sharing

#     class Meta:
#         unique_together = ('user', 'movie_id')  # Ensures no duplicate movies in the watchlist for the same user
#         verbose_name = "Watchlist Entry"
#         verbose_name_plural = "Watchlist Entries"

#     def __str__(self):
#         return f"{self.user.username}'s Watchlist: {self.movie_title}"

#     def get_absolute_url(self):
#         """
#         Returns the URL for this specific watchlist entry
#         """
#         return f"/watchlist/{self.slug}/"