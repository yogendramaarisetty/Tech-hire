from django.db import models
from django.utils import timezone
# Create your models here.
class Challenge(models.Model):
    Slug = models.SlugField()
    Title = models.CharField(max_length=120)
    Description = models.TextField(max_length=120)
    College = models.CharField(max_length=120)
    Duration = models.DurationField()
    Active = models.BooleanField()
    
    def __str__(self):
        return f'{self.Title}'
    def is_active(self):
        return f'{self.Active}'

class Question(models.Model):
    Slug = models.SlugField()
    Title = models.CharField(max_length=120)
    Type= models.CharField(max_length=120)
    Desciption = models.TextField(max_length=320)
    sample_inputs= models.TextField(max_length=50)
    sample_output= models.TextField(max_length=50)
    challenge = models.ForeignKey(Challenge,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.Title}'