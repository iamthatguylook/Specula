from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    studentID = models.CharField(max_length=500,primary_key=True)
    phoneNumber = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    password = models.CharField(max_length=15,null = True)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    professorID = models.CharField(max_length=500)
    phoneNumber = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    password = models.CharField(max_length=15,null=True)
    
    def __str__(self):
        return self.name

    

