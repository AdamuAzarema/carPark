from rest_framework import serializers
from .models import ParkingLot, ParkingSpace


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'
