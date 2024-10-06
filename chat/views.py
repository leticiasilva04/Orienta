from django.shortcuts import render, redirect

def room(request, room_name):

    chat = "Chat"
    return render(request, 'room.html', {
        'room_name': chat
    })

def home_chat(request):
    return render(request, 'home_chat.html')