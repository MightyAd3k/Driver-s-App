from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from reservation.models import (
    Driver,
    Vehicle,
    Parking
)
from reservation.forms import DriverModelForm, VehicleModelForm, ParkingModelForm
from reservation.models import parking_types


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddDriver(CreateView):
    model = Driver
    form_class = DriverModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('drivers')


class DetailsDriver(DetailView):
    model = Driver
    template_name = 'driver_detail_view.html'


class UpdateDriver(UpdateView):
    model = Driver
    form_class = DriverModelForm
    template_name = 'form.html'


class DeleteDriver(DeleteView):
    model = Driver
    template_name = 'delete.html'
    success_url = reverse_lazy('drivers')

    # def get_queryset(self):
    #     nationality = self.request.GET.get('nationality')
    #     drivers = models.Driver.objects.all()
    #     if nationality is not None:
    #         drivers = drivers.filter(nationality=nationality)
    #     return drivers


class DriversList(View):
    def get(self, request):
        nationality = request.GET.get('nationality')
        drivers = Driver.objects.all()
        if nationality is not None:
            drivers = drivers.filter(nationality=nationality)
        context = {'drivers': drivers}
        return render(request, 'drivers.html', context)

    def post(self, request):
        nationality = request.POST['nationality']
        drivers = Driver.objects.filter(nationality=nationality)
        context = {'drivers': drivers}
        return render(request, 'drivers1.html', context)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddVehicle(CreateView):
    model = Vehicle
    form_class = VehicleModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('vehicles')


class DetailsVehicle(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail_view.html'


class UpdateVehicle(UpdateView):
    model = Vehicle
    form_class = VehicleModelForm
    template_name = 'form.html'


class DeleteVehicle(DeleteView):
    model = Vehicle
    template_name = 'delete.html'
    success_url = reverse_lazy('vehicles')


class VehiclesList(View):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        context = {'vehicles': vehicles}
        return render(request, 'vehicles.html', context)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddParking(CreateView):
    model = Parking
    form_class = ParkingModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('parkings')


class DetailsParking(DetailView):
    model = Parking
    template_name = 'parking_details_view.html'


class UpdateParking(UpdateView):
    model = Parking
    form_class = ParkingModelForm
    template_name = 'form.html'


class DeleteParking(DeleteView):
    model = Parking
    template_name = 'delete.html'
    success_url = reverse_lazy('parkings')


class ParkingsList(View):
    def get(self, request):
        parkings = Parking.objects.all()
        context = {
            'parkings': parkings,
            'type': parking_types
        }
        return render(request, 'parkings.html', context)
