from django.shortcuts import render, redirect ,reverse
from .models import Room
from .forms import RoomForm

# Create your views here.

# INDEX
def home(request):
    rooms = Room.objects.all()
    context = { 
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)


# ROOMS VIEWS
def room(request,pk):
    room = Room.objects.get(id=pk)
    context={
        'room': room
    }
    
    return render(request, 'base/room.html', context)

# CREATE A  ROOM
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