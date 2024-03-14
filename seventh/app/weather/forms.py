from .models import City
from django import forms  #, TextInput


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'city',
                'name': 'city',
                'placeholder': 'Введите город'
            })
        }
