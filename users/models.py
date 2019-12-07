from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(default="NA",max_length=24)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    rollnumber = models.CharField(default="NA",max_length=20)
    college = models.CharField(default="NA",max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'
