
from User.serializer import CustomProfessorSerializer
from rest_framework.authtoken.models import Token

# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register

  
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = CustomProfessorSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)