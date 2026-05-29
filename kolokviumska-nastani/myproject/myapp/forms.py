from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    bands = forms.CharField(
        required=False,
        help_text="Внеси ги бендовите одделени со запирка"
    )

    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'poster', 'is_outside']