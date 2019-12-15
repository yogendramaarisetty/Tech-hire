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
    path('submitted/',auth_views.LogoutView.as_view(template_name="challenge/home.html"),name="logout"),
    path('tests/',views.challenges,name='tests'),
    path('index/',views.index,name='index'),
    url(r'^candidate_form/testInstruction/(?P<pk>\d+)/$', views.test_instruction, name='test_instruction'),
    url(r'^candidate_form/(?P<challenge_id>\d+)/$', views.candidate_form, name='candidate_form'),
    path('login/',auth_views.LoginView.as_view(template_name="challenge/login.html"),name="login"),
]