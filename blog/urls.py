from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<slug:slug>/', views.details, name='details'),
    path('<slug:slug>/comment/', views.comment, name='comment')
]
