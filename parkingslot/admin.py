from django.contrib import admin

# Register your models here.
from .models import CarModel, ParkingSlot

admin.site.register(CarModel)
admin.site.register(ParkingSlot)