from datetime import datetime

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from reservation.models import (
    Driver,
    Vehicle,
    Parking, ParkingReservation
)


class DriverModelForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class ParkingModelForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = '__all__'


# class ParkingPlaceModelForm(forms.ModelForm):
#     class Meta:
#         model = ParkingPlace
#         fields = '__all__'


class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = ParkingReservation
        fields = ['occupied_from', 'occupied_to']
        widgets = {
            'occupied_from': AdminSplitDateTime(),
            'occupied_to': AdminSplitDateTime()
        }
