from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('loginProfessor/',views.loginProfessor,name='loginProfessor/'),
    path('loginStudent/',views.loginStudent,name='loginStudent/')
]