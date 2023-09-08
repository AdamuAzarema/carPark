from django.urls import path
from .views import ParkingLotListCreateView, ParkingSpaceListCreateView

urlpatterns = [
    path('parking_lots/', ParkingLotListCreateView.as_view(), name='parking_lot-list-create'),
    path('parking_spaces/', ParkingSpaceListCreateView.as_view(), name='parking_space-list-create'),
]
