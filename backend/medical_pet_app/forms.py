from django import forms
from .models import Medical_pet
from django.contrib.gis.geos import Point

class MedForm(forms.ModelForm):
    class Meta:
        model = Medical_pet
        fields = '__all__'

