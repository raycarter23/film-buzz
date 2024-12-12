from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    date_joined = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.user.username

