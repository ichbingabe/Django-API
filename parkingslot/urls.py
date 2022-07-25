from django.urls import path
from .views import CarModelDetailChangeAndDelete, ParkingSlotDetailChangeAndDelete, ParkingSlotListAndCreate, CarModelListAndCreate

urlpatterns = [
    path('parkingspot/<int:pk>/', ParkingSlotDetailChangeAndDelete.as_view()),
    path('parkingspot/', ParkingSlotListAndCreate.as_view()),
    path('car/<int:pk>', CarModelDetailChangeAndDelete.as_view()),
    path('car/', CarModelListAndCreate.as_view())
]