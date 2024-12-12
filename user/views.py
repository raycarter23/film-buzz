from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required
def view_profile(request):
    profile,created = UserProfile.objects.get_or_create(user=request.user)

    return render(request,'user/profile.html', {'profile': profile})

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

