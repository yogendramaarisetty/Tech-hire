from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('index/',views.index,name='index'),

]
