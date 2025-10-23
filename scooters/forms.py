from django import forms
from .models import Scooter

class ScooterForm(forms.ModelForm):
    class Meta:
        model = Scooter
        fields = ['name', 'identifier', 'battery_level', 'is_available', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }