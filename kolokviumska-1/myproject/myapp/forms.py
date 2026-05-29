from django import forms
from django.core.exceptions import ValidationError
from .models import Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        baker = cleaned_data.get('baker')

        if baker:
            # броиме колку торти има пекарот
            broj = Cake.objects.filter(baker=baker).count()

            # ако editираме, не ја бројме тековната торта
            if self.instance.pk:
                broj = broj - 1

            if broj >= 10:
                raise ValidationError("Пекарот веќе има 10 торти!")

        return cleaned_data