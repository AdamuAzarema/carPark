from rest_framework import serializers
from .models import ParkingLot, ParkingSpace, User, Vehicle, Transaction

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'

class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

