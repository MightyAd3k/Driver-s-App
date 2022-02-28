from django.db import models

vehicle_types = (
    (1, 'car'),
    (2, 'truck')
)

parking_types = (
    (1, 'cars'),
    (2, 'trucks')
)


class Driver(models.Model):
    name = models.CharField(max_length=12)
    surname = models.CharField(max_length=12)
    nationality = models.CharField(max_length=3)


class Vehicle(models.Model):
    type = models.CharField(choices=vehicle_types)
    license_place = models.CharField(max_length=10)
    driver_name = models.OneToOneField(Driver, on_delete=models.CASCADE)


class Parking(models.Model):
    type = models.CharField(choices=parking_types)
    number_of_places = models.IntegerField()


class ParkingPlace(models.Model):
    number_of_place = models.IntegerField()
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)


class ParkingReservation(models.Model):
    occupied_from = models.DateTimeField()
    occupied_to = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE)
