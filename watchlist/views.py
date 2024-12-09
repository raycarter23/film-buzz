from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Watchlist
from movies.models import Movie
import requests

# Create your views here.
@login_required
def add_to_watchlist(request, movie_id):
    """
    Adds a movie to the user's watchlist
    """
    movie = Movie.objects.filter(id=movie_id).first()
    if not movie:
        tmdb_movie_url = f"https://api.moviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}"
        response = requests.get(tmdb_movie_url)

        if response.status_code == 200:
            data = response.json()
            movie = Movie.objects.create(
                id = movie_id,
                title = data['title'],
                release_date = data['release_date'],
                tmdb_id = movie_id,
                poster = f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            )
    
    else:
        return redirect('watchlist')
    
    watchlist = Watchlist.objects.get_or_create(user=request.user, movie='movie')
    if watchlist:
        watchlist.save()

    return redirect('watchlist')
