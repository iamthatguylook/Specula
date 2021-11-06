from django.urls import path
from . import views

urlpatterns = [

    # API restframework  VIEWS
    path('api/roomList',
         views.RoomList.as_view(), name='RoomList'),
    path('api/roomDetail/<str:pk>/',
         views.RoomDetail.as_view(), name='RoomDetail'),
    path('api/Student/<str:pk>/',
         views.StudentDetailOnID.as_view(), name='studentDetails/ID'),

    path('api/registerationStudent/ListAllStudents/',
         views.StudentList.as_view(), name='registerationStudent/ListALLStudents/'),
    path('api/registerationStudent/<str:pk>/',
         views.StudentDetail.as_view(), name='registerationStudent/int<pk>/'),
    path('api/registerationProfessor/ListAllProfessors/',
         views.ProfessorList.as_view(), name='registerationProfessor/ListALLProfessors/'),
    path('api/registerationProfessor/<int:pk>/',
         views.ProfessorDetail.as_view(), name='registerationProfessor/int<pk>/'),
    path('api/TimeLine/',
         views.TimeLineList.as_view(), name='api/ListTimeLine/'),

    path('api/TimeLine/<str:currentexam>/<str:id>/',
         views.TimeLineListBasedOnStudent.as_view(), name='api/ListTimeLine/certain'),
    path('api/TimeLine/<str:currentexam>/',
         views.TimeLineListBasedOnCurrentexam.as_view(), name='api/ListTimeLine/exam')

]
