from django.shortcuts import render
from .models import Student
from .models import Professor
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'loginProfessor.html')

def loginProfessor(request):
    Professors = Professor.objects.all()
    return render(request,'loginProfessor.html',{'Professors':Professors})

def loginStudent(request):
    Students = Student.objects.all()
    return render(request,'loginStudent.html',{'Students':Students})