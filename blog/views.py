from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html',{'posts':posts})

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/details.html', {'post':post})