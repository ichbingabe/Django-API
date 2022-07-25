from django.db import models
from django.forms import ValidationError


def restrict_amount(value):
    if CarModel.objects.filter(parking_slot=value).count() >= 3:
        raise ValidationError('Team already has maximal amount of rounds (3)')


class ParkingSlot(models.Model):
    parking_slot_id = models.AutoField(primary_key=True)
    responsible_name = models.CharField(max_length=70)
    apartment = models.CharField(max_length=10)
    block = models.CharField(max_length=10)

    def __str__(self) :
        return str(self.parking_slot_id)


class CarModel(models.Model):
    parking_slot = models.ForeignKey(ParkingSlot, validators=(restrict_amount, ),on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=8, primary_key=True)
    model = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=10)
    brand = models.CharField(max_length=70)
    
    def __str__(self) :
        return str(self.license_plate)