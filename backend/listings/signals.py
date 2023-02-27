from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.gis.geos import Point
from django.utils import timezone
from .models import Pet
from medical_pet_app.models import Medical_pet
from datetime import datetime
import datetime


@receiver(pre_save, sender=Pet)
def check_location(sender, instance, **kwargs):
    if  instance.location is None:
        instance.location = Point(53.95369,27.62643)
@receiver(pre_save, sender=Pet)
def calculate_age(sender, instance, **kwargs):
    today = datetime.date.today()
    age_seconds = (today - instance.dob).total_seconds()
    age_weeks = age_seconds /604800
    round_weeks = float('%.2f' % age_weeks)
    print(type(round_weeks))
    instance.age = round_weeks





