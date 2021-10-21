from django.shortcuts import render
from .models import Professor
from .models import Student
from .serializers import StudentSerializer
from .serializers import ProfessorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


class StudentList(APIView):
    permission_classes = [IsAuthenticated]
    #List all Students when API requests are sent to API
    def get(self, request, format=None):
        students = Student.objects.all()
        serializerForStudent = StudentSerializer(students,many=True)
        return Response(serializerForStudent.data)
    
    def post(self,request,format=None):
        serializerForUploadingStudent = StudentSerializer(data=request.data)
        if serializerForUploadingStudent.is_valid():
            serializerForUploadingStudent.save()
            return Response(serializerForUploadingStudent.data,status=status.HTTP_201_CREATED)
        return Response(serializerForUploadingStudent.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a Student instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProfessorList(APIView):
    #List all Students when API requests are sent to API
    def get(self, request, format=None):
        professors = Professor.objects.all()
        serializerForProfessor = ProfessorSerializer(professors,many=True)
        return Response(serializerForProfessor.data)
    
    def post(self,request,format=None):
        serializerForUploadingProfessor = ProfessorSerializer(data=request.data)
        if serializerForUploadingProfessor.is_valid():
            serializerForUploadingProfessor.save()
            return Response(serializerForUploadingProfessor.data,status=status.HTTP_201_CREATED)
        return Response(serializerForUploadingProfessor.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfessorDetail(APIView):
    """
    Retrieve, update or delete a Professor instance.
    """
    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        professor= self.get_object(pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        professor = self.get_object(pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


