from django.db import models
import uuid


class character (models.Model):
    level = models.IntegerField()
    name =models.CharField(max_length=50)
    TID = models.UUIDField('Character ID', primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField()

    def __str__(self):
        return self.name

    
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




