from django.db import models
import uuid


class character (models.Model):
    level = models.IntegerField
    avatar = models.ImageField()
    
class chores(models.Model):
    name = models.CharField(max_length=250)
    points = models.IntegerField()
    character = models.OneToOneField(character, on_delete=models.CASCADE)

class user(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250)
    choresHaving = models.ManyToManyField(chores, blank=True)




