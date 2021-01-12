from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authorization.models import User, UserProfile


class LoginForm(forms.ModelForm):
    pass

class RegisrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        # field_classes = {'username': UsernameField}

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user', 'slug')
