from django import forms
from reservation.models import (
    Driver,
    Vehicle,
    Parking,
    ParkingReservation
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


class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = ParkingReservation
        exclude = ['parking_place']
        widgets = {
            'from_day': forms.SelectDateWidget(),
            'from_hour': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'to_day': forms.SelectDateWidget(),
            'to_hour': forms.TimeInput(attrs={'type': 'time'}),
        }
