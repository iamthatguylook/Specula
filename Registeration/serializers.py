from rest_framework import serializers
from .models import Student
from .models import Professor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','studentID','phoneNumber','degree']



class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name','professorID','phoneNumber','degree']

