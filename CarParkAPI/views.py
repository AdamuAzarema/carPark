from rest_framework import generics
from .models import ParkingLot, ParkingSpace, User, Vehicle, Transaction
from .serializers import ParkingLotSerializer, ParkingSpaceSerializer, UserSerializer, VehicleSerializer, TransactionSerializer

class ParkingLotListCreateView(generics.ListCreateAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

class ParkingSpaceListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

