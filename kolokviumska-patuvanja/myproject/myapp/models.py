from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum


# Create your models here.
class TourGuide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Travel(models.Model):
    destination = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.destination} {self.tour_guide}"

    def clean(self):
        if self.tour_guide:

            count = Travel.objects.filter(tour_guide=self.tour_guide).count()
            if count >= 5:
                raise ValidationError("Водачот веќе има 5 дестинации")

            total = Travel.objects.filter(tour_guide=self.tour_guide).aggregate(Sum('price'))['price__sum'] or 0
            if total + self.price > 50000:
                raise ValidationError('Вкупната цена надминува 50000')

            if Travel.objects.filter(destination=self.destination).exists():
                raise ValidationError('Дестинација со ова име веќе постои')

