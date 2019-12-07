from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            rollnumber = form.cleaned_data.get('username')
            college = form.cleaned_data.get('college')
            pwd = form.cleaned_data.get('password1')
            fullname = form.cleaned_data.get('firstname')+" "+form.cleaned_data.get('lastname')
            user = User.objects.all().filter(username=rollnumber).first()
            profile = Profile(user=user,rollnumber=rollnumber,college=college,fullname=fullname)
            profile.save()            
            messages.success(request, f'Congrats account for {rollnumber} is created! \n Now try to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


def profile(request):
    return render(request,"users/profile.html")
