from django.urls import path 
from . import views
from .views import StudentRegisteration_View
urlpatterns = [
    path('registerationProfessor/',views.registerationProfessor,name='registerationProfessor/'),
    path('registerationStudent/',views.registerationStudent,name='registerationStudent/'),
    # API restframework  VIEWS
    path('api/registerationStudent/ListAllStudents/', views.StudentList.as_view(),name='registerationStudent/ListALLStudents/'),
    path('api/registerationStudent/<int:pk>/', views.StudentDetail.as_view(),name='registerationStudent/int<pk>/'),
    path('api/registerationProfessor/ListAllProfessors/', views.ProfessorList.as_view(),name='registerationProfessor/ListALLProfessors/'),
    path('api/registerationProfessor/<int:pk>/', views.ProfessorDetail.as_view(),name='registerationProfessor/int<pk>/'),
    path('api/registerationStudent/registered/', views.StudentRegisteration_View,name='registerStudent'),
]