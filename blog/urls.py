from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.details, name='details'),
    path('<slug:category_slug>/<slug:slug>/comment/', views.comment, name='comment'),
    path('<slug:category_slug>/<slug:slug>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/', views.category, name='category'),
    path('summernote/', include('django_summernote.urls')),
]
