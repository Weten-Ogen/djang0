from django.shortcuts import render, redirect 
from django.contrib import messages
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout

# Create your views here.
# Login Page

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username Doesnt Exist')

        user = authenticate(request,username=username,password=password)
       
        if user is not None:
            login(request,user)
            return redirect('base:home')
        else: 
            messages.error(request, 'Username or password does not exist')
            
    context = {
       

    }
    return render(request, 'base/login_registry.html',context)



def logoutUser(request):
    logout(request)
    return redirect('base:home')


# INDEX
def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
            Q(topic__name__icontains=q)|
            Q(name__icontains=q)|
            Q(description__icontains=q)
            )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = { 
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
    }
    return render(request, 'base/home.html', context)


# ROOMS VIEWS
def room(request,pk):
    room = Room.objects.get(id=pk)
    context={
        'room': room
    }
    
    return render(request, 'base/room.html', context)

# CREATE ROOM
@login_required(login_url="base:login")
def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':form
    }
    return render(request, 'base/room-form.html', context)

# UPDATE ROOM

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {
        'form':form
    }
    return render(request,'base/room-form.html',context)

# DELETE ROOM 

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect("/")
    context ={
        'room': room
    }
    return render(request, 'base/delete-form.html',context)