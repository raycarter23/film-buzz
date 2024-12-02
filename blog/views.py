from django.shortcuts import render
from blog.models import Post

# Create your views here.

def blog(request):
    posts = Post.object.all()
    return render(request, 'blog/blog.html',{'posts':posts})

def details(request):
    return render(request, 'blog/details.html')