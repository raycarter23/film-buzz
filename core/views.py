from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from blog.models import Post
from django.db.models import Count

# Create your views here.

def home(request):
    trending_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:3]
    return render(request, 'core/home.html', {'trending_posts':trending_posts})

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        # Check if the form is valid
        if form.is_valid():
            user = form.save()

            # get the raw password
            raw_password = form.cleaned_data['password1']

            # authenticate the user
            user = authenticate(username=user.username, password=raw_password)

            # login the user
            login(request, user)

            return redirect('home')

    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # Check if the form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})
        
