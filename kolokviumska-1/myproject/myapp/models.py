from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Baker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

class Cake(models.Model):
    name = models.CharField(max_length=20)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
