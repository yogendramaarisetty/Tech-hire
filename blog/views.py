from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import datetime

def projecthome(request):
    return HttpResponse("<h1> PROJECT HOMEPAGE</h1>")

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
