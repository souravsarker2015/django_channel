from django.urls import path

from chat.views import homepage, room

urlpatterns = [
    path('', homepage, name='home'),
    path('room/', room, name='room'),
]
