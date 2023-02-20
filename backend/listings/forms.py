from django import forms
from .models import Pet
from django.contrib.gis.geos import Point

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name','age','pet_breed','chip_num','pet_gender','dob','pet_color','pet_disc','owner','created_at','location', 'latitude', 'longitude','pet_image1','pet_image2','pet_image3','qr_code_img']
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    def clean(self):
        data = super().clean()
        latitude = data.pop('latitude')
        longitude = data.pop('longitude')
        data['location'] = Point(latitude,longitude,srid=4326)
        return data
      
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        location = self.initial.get('location')
        if isinstance(location,Point):
            self.initial['latitude'] = location.tuple[0]
            self.initial['longitude'] = location.tuple[1]