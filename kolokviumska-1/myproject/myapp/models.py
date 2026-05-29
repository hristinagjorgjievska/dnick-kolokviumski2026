from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
