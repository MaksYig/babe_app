from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.gis.geos import Point
from .models import Pet

@receiver(pre_save, sender=Pet)
def check_location(sender, instance, **kwargs):
    if  instance.location is None:
        instance.location = Point(53.95369,27.62643)

