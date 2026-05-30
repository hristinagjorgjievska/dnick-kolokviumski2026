from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    authors = models.ManyToManyField(Author)
