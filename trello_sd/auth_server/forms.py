from django import forms
from django.contrib.auth.forms import AuthenticationForm

# from .models import AppUser
from django.contrib.auth.models import User


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password',)