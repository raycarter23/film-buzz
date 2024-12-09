from django.urls import path, include 
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<slug:slug>/', views.details, name='details'),
    path('<slug:slug>/comment/', views.comment, name='comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('summernote/', include('django_summernote.urls')),
]
