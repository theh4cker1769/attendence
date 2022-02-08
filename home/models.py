from django.db import models

# Create your models here.

class Student(models.Model):
    ien = models.IntegerField(null=False, blank=False, default='')
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    attendence = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
