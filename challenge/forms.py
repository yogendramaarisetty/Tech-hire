from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label="Rollnumber")
    fullname = forms.CharField(label="Full Name")
    
    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
        }
        fields = ['username','fullname','email','password1','password2']