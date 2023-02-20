from rest_framework import serializers
from listings.models import Pet
from users.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class PetSerializer(serializers.ModelSerializer):
    pet_image1 = serializers.ImageField(required=False)
    pet_image2 = serializers.ImageField(required=False)
    pet_image3 = serializers.ImageField(required=False)
    class Meta:
        model = Pet
        fields = '__all__'


class PetListingIDSerializer(serializers.ModelSerializer):
   
    class Meta:
        model =Pet
        fields = '__all__'
        depth = 1