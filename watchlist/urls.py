from django.urls import path 
from . import views

urlpatterns = [
    path('', views.view_watchlist, name='watchlist'),
    path('add/<int:movie_id>', views.add_to_watchlist, name='add_to_watchlist'),
    # path('remove/<int:movie_id>', views.remove_watchlist, name='remove_watchlist'),
    path('search/', views.search_movies, name='search_movies'),
]