from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ParkingLot, ParkingSpace
from .serializers import ParkingLotSerializer, ParkingSpaceSerializer


class ParkingLotListCreateView(generics.ListCreateAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer


class ParkingSpaceListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
