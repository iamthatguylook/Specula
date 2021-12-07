from django.urls import path
from .views import registration_view
from .views import CustomAuthToken
from User import views
app_name = 'User'
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register', registration_view, name="create_user"),
    path('login', obtain_auth_token, name="login"),
    path('userDetails/<str:pk>', views.CustomAuthToken.as_view())
]