from django.db import models

# Create your models here.

# Parking Lot Model

class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    total_spaces = models.PositiveIntegerField()
    available_spaces = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    night_rate = models.DecimalField(max_digits=10, decimal_places=2)

# Parking Space Model

class ParkingSpace(models.Model):
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    space_number = models.PositiveIntegerField()
    SIZE_CHOICES = [
        ('Compact', 'Compact'),
        ('Standard', 'Standard'),
        ('Handicap', 'Handicap'),
    ]
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    AVAILABILITY_CHOICES = [
        ('Occupied', 'Occupied'),
        ('Vacant', 'Vacant'),
    ]
    availability = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES)

# User Model

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    # Hashed password should be stored
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Attendant', 'Attendant'),
        ('Customer', 'Customer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# Vehicle Model

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=20)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=50)

# Transaction Model

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    amount_paid = models.DecimalField(
    max_digits=10, decimal_places=2, null=True, blank=True)
