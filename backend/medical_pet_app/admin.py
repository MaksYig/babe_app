import json
import logging
from django.db.models import JSONField 
from django.contrib import admin
from .models import Medical_pet
from .forms import MedForm
from django.forms import widgets
# Register your models here.

admin.site.register(Medical_pet)
