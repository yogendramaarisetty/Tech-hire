from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, views
from django.conf.urls import url

urlpatterns = [
    
    
    path('register/',views.challenge_register,name='challenge_register'),
    path(r'^account_activation_sent/$',views.account_activation_sent,name='account_activation_sent'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name='activate'),
    path('submitted/',auth_views.LogoutView.as_view(template_name="challenge/logout.html"),name="logout"),
    path('tests/',views.challenges,name='tests'),
    path('index/',views.index,name='index')
    # path('login/',auth_views.LoginView.as_view(template_name="challenge/login.html"),name="login"),
]