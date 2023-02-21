from django.contrib.gis.db import models
from random import choices
from django.utils import timezone
from django.contrib.gis.geos import Point
from users.models import Profile

    


class Pet(models.Model):
    gender_choises =[('male', 'male'), ('female', 'female')]
    
    
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True,null=True)
    dob = models.DateTimeField('Date of birth:',blank=True, null=True)
    pet_breed = models.CharField(max_length=30,blank=True,null=True)
    pet_disc=models.TextField(blank=True,null=True)
    pet_color=models.CharField(blank=True,null=True,max_length=100)
    chip_num = models.CharField('Chip Number',max_length=30,blank=True,null=True)
    pet_gender = models.CharField('Gender',max_length=30,blank=True,null=True,choices=gender_choises)
    
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    location = models.PointField(blank=True,null=True, srid=4326)
    pet_image1 = models.ImageField(blank=True,null=True, upload_to="pet_images/%Y/")
    pet_image2 = models.ImageField(blank=True,null=True,upload_to="pet_images/%Y/")
    pet_image3 = models.ImageField(blank=True,null=True,upload_to="pet_images/%Y/")
    qr_code_img = models.ImageField(blank=True,null=True,upload_to="pet_images/qr_code/%Y/")
    owner = models.ForeignKey(to=Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name