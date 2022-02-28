from django import forms

from reservation import models


class DriverModelForm(forms.ModelForm):
    class Meta:
        model = models.Driver
        fields = '__all__'
