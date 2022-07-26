from rest_framework import serializers
from .models import ParkingSlot, CarModel


class ParkingSlotSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ParkingSlot
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = CarModel
        fields = '__all__'
