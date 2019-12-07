from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label="Rollnumber")
    college = forms.CharField()
    firstname = forms.CharField(label="First Name")
    lastname = forms.CharField(label="Last Name")
    
    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
        }
        fields = ['username','firstname','lastname','email','college','password1','password2']