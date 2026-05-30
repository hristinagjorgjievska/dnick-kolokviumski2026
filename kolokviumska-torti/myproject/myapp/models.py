from django.db import models

# Create your models here.
class Baker(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Cake(models.Model):
    name = models.CharField(max_length=20)
    #Овде on_delete=models.SET_NULL поради условот ,,Кога се брише пекарот, неговите торти по случаен избор се додаваат на останатите пекари''
    baker = models.ForeignKey(Baker, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


