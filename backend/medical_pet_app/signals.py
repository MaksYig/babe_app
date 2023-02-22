from django.contrib.auth import get_user_model
from django.dispatch import receiver
from listings.models import Pet
from .models import Medical_pet
from django.db.models.signals import post_save


@receiver(post_save,sender=Pet)
def createPetMedical(sender,instance,created,**kwargs):
    if created:
        Medical_pet.objects.create(pet=instance)

@receiver(post_save,sender=Pet)
def savePetMedical(sender,instance,**kwargs):
    instance.pet.save()