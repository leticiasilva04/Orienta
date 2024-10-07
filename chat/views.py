from django.shortcuts import render, redirect

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

def home_chat(request):
    return render(request, 'home_chat.html')