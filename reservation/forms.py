from django import forms

from reservation.models import (
    Driver,
    Vehicle,
    Parking
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
