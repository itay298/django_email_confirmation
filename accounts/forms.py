from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password1', 'password2']