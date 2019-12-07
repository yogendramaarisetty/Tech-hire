from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.Field(max_length=50)
    cateogory= models.CharField(max_length=50)
    level = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    sample_input = models.CharField(max_length=50)
    sample_output = models.CharField(max_length=50)
    testcase_inputs = models.FileField()
    testcase_outputs = models.FileField()

    def __str__(self):
        return f'{self.title} ({self.level})'
