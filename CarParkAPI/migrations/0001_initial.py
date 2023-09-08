# Generated by Django 4.2.5 on 2023-09-08 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('total_spaces', models.PositiveIntegerField()),
                ('available_spaces', models.PositiveIntegerField()),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('night_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_number', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('Compact', 'Compact'), ('Standard', 'Standard'), ('Handicap', 'Handicap')], max_length=20)),
                ('availability', models.CharField(choices=[('Occupied', 'Occupied'), ('Vacant', 'Vacant')], max_length=20)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarParkAPI.parkinglot')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Attendant', 'Attendant'), ('Customer', 'Customer')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('license_plate', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarParkAPI.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('entry_time', models.DateTimeField()),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('parking_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarParkAPI.parkinglot')),
                ('parking_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarParkAPI.parkingspace')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarParkAPI.user')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarParkAPI.vehicle')),
            ],
        ),
    ]
