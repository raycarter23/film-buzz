from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html',{'posts':posts})

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'blog/details.html', {'post': post, 'comments': comments, 'form': form})

def comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('details', slug=slug)
    else:
        form = CommentForm()
    comments = post.comments.all()
    return render(request, 'blog/details.html', {'post': post, 'comments': comments, 'form': form})

def delete_comment(request, comment_id, slug):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and comment.user == request.user:
        comment.delete()
        return redirect('details', slug=slug)
        