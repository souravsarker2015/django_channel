from django.db import models


# Create your models here.

class Chat(models.Model):
    room_no = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
