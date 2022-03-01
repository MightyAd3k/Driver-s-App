from django import forms

from reservation import models


class DriverModelForm(forms.ModelForm):
    class Meta:
        model = models.Driver
        fields = '__all__'


class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = '__all__'
