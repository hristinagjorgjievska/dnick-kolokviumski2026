from django.forms import ModelForm
from .models import Travel

class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = ["image", "destination", "price", "duration"]