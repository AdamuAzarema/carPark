from django.db import models

# Create your models here.

class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    total_spaces = models.PositiveIntegerField()
    available_spaces = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    night_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ParkingSpace(models.Model):
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    space_number = models.PositiveIntegerField()
    size = models.CharField(max_length=20, choices=[('Compact', 'Compact'), ('Standard', 'Standard'), ('Handicap', 'Handicap')])
    availability = models.CharField(max_length=20, choices=[('Occupied', 'Occupied'), ('Vacant', 'Vacant')])

    def __str__(self):
        return f"Space {self.space_number} - {self.lot.name}"

