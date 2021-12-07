
from Registeration.models import Student
from User.serializer import CustomUserSerializer,UserDetailSerializer


# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register

  
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Registeration.serializers import StudentSerializer

from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from User.models import User
from django.http import Http404

 
@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		
		serializer = CustomUserSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			student = Student(name = account.name,studentID = account.username)
			student.save()
			data['name'] = account.name
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)


class CustomAuthToken(APIView):
	def get_object(self,pk):
		try:
			return User.objects.get(email=pk)
		except User.DoesNotExist:
			raise Http404	
	
	def get(self, request, pk, format=None):
       		user = self.get_object(pk)
        	serializer = UserDetailSerializer(user)
        	return Response(serializer.data)


	