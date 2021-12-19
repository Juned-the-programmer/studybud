from django.shortcuts import render , HttpResponse , redirect
from room.models import * 
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

# Create your views here.
@login_required(login_url="login")
def index(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__contains=q) | 
        Q(name__contains=q) |
        Q(description__contains=q)
    )

    Topic_list = Topic.objects.all()
    Room_Count = Room.objects.all().count()
    room_message = Message.objects.filter(user = User.objects.get(username=request.user.username))
    print(Room_Count)
    context = {
        'Topic_list' : Topic_list,
        'Room_count' : Room_Count,
        'rooms' : rooms,
        'room_message' : room_message
    }
    return render(request , "pages/index.html" , context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user_login = auth.authenticate(username=username , password=password)
        if user_login is not None:
            auth.login(request,user_login)
            messages.success(request, "Login Success")
            return redirect('index')
        else:
            print("Login Error")
            messages.error(request, "Invalid Login")

    return render(request , "pages/login.html")

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username'].lower()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user_signup = User.objects.create_user(username=username, password=password , first_name =first_name, last_name =last_name , email = email)
            user_signup.save()
            return redirect('login')

    return render(request , "pages/signup.html")

def setting(request):
    user_data = User.objects.get(username = request.user.username)

    if request.method == 'POST':
        user_data.first_name = request.POST['first_name']
        user_data.last_name = request.POST['last_name']
        user_data.email = request.POST['email']
        user_data.username = request.POST['username']

        user_data.save()
        return redirect('index')

    context = {
        'user_data' : user_data
    }
    return render(request , "pages/setting.html" , context)

def logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    if request.method == 'POST':
        user = User.objects.get(Username = request.user.username)

        data = request.user.profile
        data.profile_picture = request.POST['profile_picture']
        data.bio = request.POST['bio']

        data.save()

    user_data = User.objects.get(username = request.user.username)
    profile = profile.objects.get(user = request.user.username)

    context = {
        'user_data' : user_data,
        'profile' : profile
    }

    return render(request , "pages/profile.html" , context)