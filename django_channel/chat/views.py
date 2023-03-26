from django.shortcuts import render

from chat.models import Chat


def homepage(request):
    return render(request, 'home.html')


def room(request):
    if request.method == 'GET':
        return render(request, 'room.html')

    if request.method == "POST":
        room_no = request.POST.get('room_no')
        name = request.POST.get('name')
        mess = Chat.objects.filter(room_no=room_no)
        messages = []
        for message in mess:
            messages.append(message.message)
        data = {
            "room_no": room_no,
            "name": name,
            "messages": messages,
        }
        return render(request, 'room.html', data)
