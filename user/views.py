from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.

@login_required
def view_profile(request):
    profile,created = UserProfile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts,6)
    page_number = request.GET.get('page')
    user_posts = paginator.get_page(page_number)

    return render(request,'user/profile.html', {'profile': profile, 'user_posts': user_posts})

# def blog(request):
#     all_posts = Post.objects.all()
#     featured_post = all_posts.first()
#     paginator = Paginator(all_posts[1:],6)
#     page_number = request.GET.get('page')
#     posts = paginator.get_page(page_number)
#     return render(request, 'blog/blog.html',{'posts':posts, 'featured_post':featured_post})

@login_required
def edit_profile(request):
    profile,created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save() 
            return redirect('profile')
    
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user/edit_profile.html', {'form': form})

