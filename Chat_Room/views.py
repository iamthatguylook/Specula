from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def room(request, room_name,user):
    return render(request, 'chatroom.html',{
        'room_name':room_name,
        'user':user
    })