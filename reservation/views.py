from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from reservation.models import (
    Driver,
    Vehicle,
    Parking,
    ParkingReservation
)
from reservation.forms import DriverModelForm, VehicleModelForm, ParkingModelForm, ReservationModelForm
from reservation.models import parking_types


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddDriver(LoginRequiredMixin, CreateView):
    model = Driver
    form_class = DriverModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('drivers')

    # def get_context_data(self, **kwargs):
    #     nationalities = []
    #     nationality = Driver.objects.get('nationality')
    #     if nationality not in nationalities:
    #         nationalities.append(nationality)
    #     return nationalities


class DetailsDriver(DetailView):
    model = Driver
    template_name = 'driver_detail_view.html'


class UpdateDriver(LoginRequiredMixin, UpdateView):
    model = Driver
    form_class = DriverModelForm
    template_name = 'form.html'


class DeleteDriver(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = 'delete.html'
    success_url = reverse_lazy('drivers')


class DriversList(View):
    def get(self, request):
        nationality = request.GET.get('nationality')
        drivers = Driver.objects.all().order_by('nationality')
        if nationality is not None:
            drivers = drivers.filter(nationality=nationality)
        unique_nationalities = Driver.objects.all().values('nationality').distinct()
        context = {'drivers': drivers, 'unique_nationalities': unique_nationalities}
        return render(request, 'driver_list.html', context)

    def post(self, request):
        nationality = request.POST['nationality']
        drivers = Driver.objects.filter(nationality=nationality).order_by('name')
        context = {'drivers': drivers}
        return render(request, 'drivers1.html', context)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddVehicle(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('vehicles')


class DetailsVehicle(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail_view.html'


class UpdateVehicle(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleModelForm
    template_name = 'form.html'


class DeleteVehicle(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'delete.html'
    success_url = reverse_lazy('vehicles')


class VehiclesList(View):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        context = {'vehicles': vehicles}
        return render(request, 'vehicles.html', context)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddParking(LoginRequiredMixin, CreateView):
    model = Parking
    form_class = ParkingModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('parkings')


class DetailsParking(DetailView):
    model = Parking
    template_name = 'parking_details_view.html'


class UpdateParking(LoginRequiredMixin, UpdateView):
    model = Parking
    form_class = ParkingModelForm
    template_name = 'form.html'


class DeleteParking(LoginRequiredMixin, DeleteView):
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


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AddParkingReservation(View):
    # model = ParkingReservation
    # form_class = ReservationModelForm
    # template_name = 'form.html'
    # success_url = reverse_lazy('detail_parking')

    def get(self, request, parking_id):
        form = ReservationModelForm()
        parking = Parking.objects.get(id=parking_id)
        context = {
            'form': form,
            'parking': parking
        }
        return render(request, 'form.html', context)

    # def post(self, request, parking_id):
    #     form = ReservationModelForm(request.POST)
    #     if form.is_valid():
    #         reservation = form.save(commit=False)
    #         reservation.parking_place = get_fst_pp()
    #         reservation.driver = request.user.driver
    #         reservation.save()
    #     return ....
