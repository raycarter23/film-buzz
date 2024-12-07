from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html',{'posts':posts})

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post = post
    #         comment.save()

    #         return redirect('details', slug=slug) 
    # else:
    #     form = CommentForm()

    return render(request, 'blog/details.html', {'post':post,})

def comment(request, slug):
    post = post.objects.get(slug=slug)
    if request.method == 'POST':
        content = request.POST['message']
        Comment(comment=content, user_id=request.user.id, post_id=post.id).save()

        return redirect('details', slug=slug)

