from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum


# Create your models here.
class Baker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()


class Cake(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    baker = models.ForeignKey(Baker, on_delete=models.SET_NULL, null=True, blank=True, related_name='cakes')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def clean(self):
        super().clean()

        if self.baker:

            count = Cake.objects.filter(baker=self.baker).exclude(pk=self.pk).count()

            if count >= 10:
                raise ValidationError('Пекарот веќе има 10 торти')

            total = Cake.objects.filter(baker=self.baker).exclude(pk=self.pk).aggregate(Sum('price'))['price__sum'] or 0
            if total + self.price > 10000:
                raise ValidationError('Сумата на тортите на пекарот надминува 10000')


            duplicate = Cake.objects.filter(name=self.name).exists()
            if duplicate:
                raise ValidationError('Веќе постои торта со такво име')