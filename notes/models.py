from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class Room_DB(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    coords = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    x = models.IntegerField()
    y = models.IntegerField()
    floor = models.IntegerField()
    n_to = models.CharField(max_length=20, null=True)
    s_to = models.CharField(max_length=20, null=True)
    e_to = models.CharField(max_length=20, null=True)
    w_to = models.CharField(max_length=20, null=True)
    u_to = models.CharField(max_length=20, null=True)
    d_to = models.CharField(max_length=20, null=True)
    region = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     currentRoom = models.IntegerField(default=0)
#     uuid = models.UUIDField(default=uuid4, unique=True)
#     def initialize(self):
#         if self.currentRoom == 0:
#             self.currentRoom = Room.objects.first().id
#             self.save()
#     def room(self):
#         try:
#             return Room.objects.get(id=self.currentRoom)
#         except Room.DoesNotExist:
#             self.initialize()
#             return self.room()

# @receiver(post_save, sender=User)
# def create_user_player(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user=instance)
#         Token.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_player(sender, instance, **kwargs):
#     instance.player.save()