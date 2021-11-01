from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    studentID = models.CharField(max_length=500,primary_key=True,unique=True)
    phoneNumber = models.CharField(max_length=500,null=True)
    degree = models.CharField(max_length=500,null=True)
    CurrentExam = models.CharField(max_length=10,null=True)
    CurrentAItimeStamp= models.CharField(max_length=6,null=True)
    CurrentAItextMessage = models.CharField(max_length=500,null=True)
    CurrentAIdangerLevel = models.CharField(max_length=500,null=True)
    #time stamp
    #message text
    #danger level
    def __str__(self):
        return self.studentID
class TimeLine(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    AItimeStamp= models.CharField(max_length=6)
    AItextMessage = models.CharField(max_length=500)
    AIdangerLevel = models.CharField(max_length=500)
    
    def __str__(self):
        return self.student

class Professor(models.Model):
    name = models.CharField(max_length=100)
    professorID = models.CharField(max_length=500)
    phoneNumber = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    password = models.CharField(max_length=15,null=True)
    
    def __str__(self):
        return self.name

    

