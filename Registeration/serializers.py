from rest_framework import serializers
from .models import Student
from .models import Professor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','studentID','phoneNumber','degree','password']



class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name','professorID','phoneNumber','degree','password']

class RegistrationStudentSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'})
    class Meta:
        model = Student
        fields = ['name','studentID','phoneNumber','degree','password','password2']
        extra_kwargs = {
                    'password' : {'write_only' : True}
        }
    def save(self):
        student1 = Student(
                studentID = self.validated_data['studentID'],
                name = self.validated_data['name'],
                phoneNumber = self.validated_data['phoneNumber'],
                degree = self.validated_data['degree']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password1 not equal to 2'})
        student1.set_password(password)
        student1.save()
        return student1