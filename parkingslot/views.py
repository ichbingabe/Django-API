from django.http import HttpResponse

from rest_framework import generics

from .serializers import CarModelSerializer, ParkingSlotSerializer
from .models import ParkingSlot, CarModel


def index(request):
    return HttpResponse("teste")


class ParkingSlotListAndCreate(generics.ListCreateAPIView):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer


class ParkingSlotDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer


class CarModelListAndCreate(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarModelDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer