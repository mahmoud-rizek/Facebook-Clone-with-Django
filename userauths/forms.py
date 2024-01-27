from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        fields = ['ful_name', 'username', 'email', 'gender', 'phone']
        