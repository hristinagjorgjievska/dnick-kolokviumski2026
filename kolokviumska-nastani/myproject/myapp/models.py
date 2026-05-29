from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    number_of_events = models.PositiveIntegerField()

class Event(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_outside = models.BooleanField()

class BandEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)