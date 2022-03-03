from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from reservation import models
from reservation.forms import DriverModelForm, VehicleModelForm


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class AddDriver(CreateView):
    model = models.Driver
    form_class = DriverModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('drivers')


class DetailsDriver(DetailView):
    model = models.Driver
    template_name = 'driver_detail_view.html'


class UpdateDriver(UpdateView):
    model = models.Driver
    form_class = DriverModelForm
    template_name = 'form.html'


class DeleteDriver(DeleteView):
    model = models.Driver
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
        drivers = models.Driver.objects.all()
        if nationality is not None:
            drivers = drivers.filter(nationality=nationality)
        context = {'drivers': drivers}
        return render(request, 'drivers.html', context)

    def post(self, request):
        nationality = request.POST['nationality']
        drivers = models.Driver.objects.filter(nationality=nationality)
        context = {'drivers': drivers}
        return render(request, 'drivers1.html', context)


class AddVehicle(CreateView):
    model = models.Vehicle
    form_class = VehicleModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('vehicles')


class DetailsVehicle(DetailView):
    model = models.Vehicle
    template_name = 'vehicle_detail_view.html'


class UpdateVehicle(UpdateView):
    model = models.Vehicle
    form_class = VehicleModelForm
    template_name = 'form.html'


class DeleteVehicle(DeleteView):
    model = models.Vehicle
    template_name = 'delete.html'
    success_url = reverse_lazy('vehicles')


class VehiclesList(View):
    def get(self, request):
        vehicles = models.Vehicle.objects.all()
        context = {'vehicles': vehicles}
        return render(request, 'vehicles.html', context)
