from django.db import models


class ParkingSlot(models.Model):
    parking_slot_id = models.AutoField(primary_key=True)
    responsible_name = models.CharField(max_length=70)
    apartment = models.CharField(max_length=10)
    block = models.CharField(max_length=10)


class CarModel(models.Model):
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    model = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=10)
    brand = models.CharField(max_length=70)
    license_plate = models.CharField(max_length=8)