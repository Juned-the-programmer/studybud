from django.shortcuts import render , HttpResponse , redirect
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def room_detail(request,pk):
    room_detail = Room.objects.get(pk=pk)
    # room_messages = Message.objects.filter(room = Room.objects.get(name=room_detail))
    room_messages = room_detail.message_set.all().order_by('-created')
    room_participant = room_detail.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = User.objects.get(username = request.user.username),
            room = Room.objects.get(pk=pk),
            body = request.POST['body']
        )
        return redirect('room_detail' , pk=room_detail.id)

    context = {
        'room_detail' : room_detail,
        'room_messages' : room_messages,
        'room_participant' : room_participant
    }
    return render(request, 'room/room_detail.html',context)

def addroom(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        topic = request.POST['topic']
        print(topic)
        room_description = request.POST['room_description']

        room = Room(
            host = User.objects.get(username=request.user.username),
            topic = Topic.objects.get(name=topic),
            name = room_name,
            description = room_description
        )
        room.save()

    topics = Topic.objects.all()
    context = {
        'topics' : topics
    }
    return render(request, 'room/addroom.html' , context)

def update_room(request,pk):
    Page = 'update_room'
    if request.method == 'POST':
        room_name = request.POST['room_name']
        topic = request.POST['topic']
        room_description = request.POST['room_description']

        room_data = Room.objects.get(pk=pk)

        room_data.name = room_name
        room_data.topic = Topic.objects.get(name=topic)
        room_data.description = room_description

        room_data.save()
        return redirect('index')

    room_data_update = Room.objects.get(pk=pk)

    context = {
        'Page' : Page,
        'room_data_update' : room_data_update
    }
    return render(request,"room/addroom.html",context)

def delete_room(request,pk):
    room = Room.objects.get(pk=pk)  

    if request.method == 'POST':
        room.delete()
        return redirect('index')
        
    context = {
        'room' : room
    }
    return render(request,"room/delete_room.html" ,context)

def user_profile(request,pk):
    Topic_list = Topic.objects.all()
    user = User.objects.get(pk=pk)
    rooms = Room.objects.filter(host = User.objects.get(username=user.username))
    room_message = Message.objects.filter(user = User.objects.get(username=user.username))
    context = {
        'Topic_list' : Topic_list,
        'user' : user,
        'rooms' : rooms,
        'room_message' : room_message
    }
    return render(request,"room/user_profile.html",context)

def delete_message(request,pk):
    room_message = Message.objects.get(pk=pk)
    if request.method == 'POST':
        room_message.delete()
        return redirect('index')

    context = {
        'room_message' : room_message
    }
    return render(request,"room/delete_message.html" , context)

def current_user_profile(request):
    user = User.objects.get(username = request.user.username)
    Topic_list = Topic.objects.all()
    rooms = Room.objects.filter(host = User.objects.get(username=user.username))
    room_message = Message.objects.filter(user = User.objects.get(username = user.username))

    context = {
        'Topic_list' : Topic_list,
        'rooms' : rooms,
        'room_message' : room_message
    }
    return render(request , "room/current_user_profile.html", context)