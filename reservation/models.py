from datetime import datetime, timedelta, date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models
from django.urls import reverse

vehicle_types = (
    ('car', 'Car'),
    ('truck', 'Truck')
)

parking_types = (
    ('cars', 'Cars'),
    ('trucks', 'Trucks')
)

nationalities = (
    ('pl', 'PL'),
    ('de', 'DE'),
    ('cz', 'CZ'),
    ('sk', 'SK'),
    ('slo', 'SLO'),
    ('lt', 'LT'),
    ('lv', 'LV'),
    ('est', 'EST'),
    ('bi', 'BI'),
    ('no', 'NO'),
    ('swe', 'SWE'),
    ('fin', 'FIN'),
    ('dk', 'DK'),
    ('be', 'BE'),
    ('nl', 'NL'),
    ('lu', 'LU'),
    ('es', 'ES'),
    ('pt', 'PT'),
    ('gb', 'GB'),
    ('irl', 'IRL'),
    ('rus', 'RUS'),
    ('ua', 'UA'),
    ('it', 'IT'),
    ('at', 'AT'),
    ('hu', 'HU'),
    ('bg', 'BG'),
    ('ro', 'RO'),
    ('srb', 'SRB'),
    ('hr', 'HR'),
    ('ch', 'CH'),
    ('al', 'AL'),
    ('mne', 'MNE'),
)


class Driver(models.Model):
    name = models.CharField(max_length=12)
    surname = models.CharField(max_length=12)
    nationality = models.CharField("Driver's nationality", max_length=3, choices=nationalities)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname} {self.get_nationality_display()}'

    def get_absolute_url(self):
        return reverse('detail_driver', args=(self.pk,))


class Vehicle(models.Model):
    type = models.CharField('Type of the vehicle', max_length=5, choices=vehicle_types)
    license_plate = models.CharField(max_length=10)
    driver_name = models.OneToOneField(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_type_display()} {self.license_plate} {self.driver_name}'

    def get_absolute_url(self):
        return reverse('detail_vehicle', args=(self.pk,))


class Parking(models.Model):
    address = models.CharField(max_length=100)
    type = models.CharField('Type of the parking', max_length=6, choices=parking_types)
    number_of_places = models.IntegerField()
    free_places = models.IntegerField()

    def __str__(self):
        return f'{self.address} {self.get_type_display()} {self.number_of_places} {self.free_places}'

    def get_absolute_url(self):
        return reverse('detail_parking', args=(self.pk,))

    def add_reservation(self):
        self.free_places -= 1
        self.save()

    def delete_reservation(self):
        self.free_places += 1
        self.save()


class ParkingPlace(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}'


def from_day_past(day):
    if day < date.today():
        raise ValidationError('This date is from past')


def to_day_past(day):
    if day < date.today():
        raise ValidationError('This date is from past')


def from_hour_past(hour):
    if hour < datetime.now().time():
        raise ValidationError('This time is from past')


class ParkingReservation(models.Model):
    from_day = models.DateField(default=datetime.today, null=True, validators=[from_day_past])
    from_hour = models.TimeField(default=datetime.now, null=True, validators=[from_hour_past])
    to_day = models.DateField(default=datetime.today() + timedelta(days=1), null=True, validators=[to_day_past])
    to_hour = models.TimeField(null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_day} {self.from_hour} {self.to_day} {self.to_hour} {self.driver}'

    def get_absolute_url(self):
        return reverse('detail_reservation', args=(self.pk,))
