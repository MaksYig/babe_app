from django.db import models
from random import choices
from django.utils import timezone

# Create your models here.

class Medical_pet(models.Model):
    med = models.JSONField(null=True)

