from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

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
