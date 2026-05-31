from django.forms import ModelForm
from .models import Cake

class CakeForm(ModelForm):
    class Meta:
        model = Cake
        fields = ["name", "price", "weight", "description", "image"]