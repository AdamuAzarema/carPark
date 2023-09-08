from django.urls import path
from .views import (
    ParkingLotListCreateView,
    ParkingSpaceListCreateView,
    UserListCreateView,
    VehicleListCreateView,
    TransactionListCreateView,
)

urlpatterns = [
    path('parking_lots/', ParkingLotListCreateView.as_view(), name='parking_lot-list-create'),
    path('parking_spaces/', ParkingSpaceListCreateView.as_view(), name='parking_space-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
]

