from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

from .models import Profile, Project, Rate


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class PostForm(forms.ModelForm):
    image = ImageField(label='')
    class Meta:
        model = Project
        fields = ('title', 'details', 'link', 'image')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'contact_info']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content', 'creativity']