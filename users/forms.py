from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None,
            'password1':None
        }
        fields = ['username','email','password1','password2']