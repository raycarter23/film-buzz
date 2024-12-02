from django.urls import path
from . import views

urlpatterns = [
    path('blog/details/', views.details, name='details')
]
