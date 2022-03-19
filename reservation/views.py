from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from reservation.models import (
    Driver,
    Vehicle,
    Parking,
    ParkingPlace, ParkingReservation
)
from reservation.forms import DriverModelForm, VehicleModelForm, ParkingModelForm, ReservationModelForm
from reservation.models import parking_types


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'base.html')


class AddDriver(LoginRequiredMixin, CreateView):
    model = Driver
    form_class = DriverModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('drivers')


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
    """
    Displays all drivers sorted by their nationalities. Allows also to select all drivers of a specific nationality
    and display them.
    """
    @staticmethod
    def get(request):
        nationality = request.GET.get('nationality')
        drivers = Driver.objects.all().order_by('nationality')

        if nationality is not None:
            drivers = drivers.filter(nationality=nationality)

        unique_nationalities = Driver.objects.all().values('nationality').distinct()
        context = {
            'drivers': drivers,
            'unique_nationalities': unique_nationalities
        }
        return render(request, 'driver_list.html', context)

    @staticmethod
    def post(request):
        nationality = request.POST['nationality']
        drivers = Driver.objects.filter(nationality=nationality).order_by('name')
        context = {
            'drivers': drivers
        }
        return render(request, 'drivers1.html', context)


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
    """
    Displays all the vehicles.
    """
    @staticmethod
    def get(request):
        vehicles = Vehicle.objects.all()
        context = {
            'vehicles': vehicles
        }
        return render(request, 'vehicles.html', context)


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
    """
    Displays all the parkings sorted by their types.
    """
    @staticmethod
    def get(request):
        parkings = Parking.objects.all().order_by('type')
        context = {
            'parkings': parkings,
            'type': parking_types
        }
        return render(request, 'parkings.html', context)


def get_first_parking_place(parking):
    """
    Returns the first parking place in a specyfic parkking lot.

    :param parking:
    :return first free parking space which 'is_free' value is True:
    """
    parking_place = ParkingPlace.objects.filter(is_free=True, parking=parking)

    return parking_place.first()


class AddParkingReservation(LoginRequiredMixin, View):
    """
    Allows to add a new parking place reservation. Using 'get_first_parking_place' function.
    Turns the 'is_free' value to False.
    """
    @staticmethod
    def get(request, parking_id):
        form = ReservationModelForm()
        parking = Parking.objects.get(id=parking_id)
        context = {
            'form': form,
            'parking': parking
        }
        return render(request, 'form.html', context)

    @staticmethod
    def post(request, parking_id):
        form = ReservationModelForm(request.POST)
        parking = Parking.objects.get(id=parking_id)

        if parking.free_places < 1:
            return HttpResponse("We're sorry, there are no more places available.")

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.parking_place = get_first_parking_place(parking)
            reservation.parking_place.is_free = False
            reservation.parking_place.save()
            reservation.save()
            parking.add_reservation()

            return redirect('/reservation/reservations/')

        context = {
            'form': form,
            'parking': parking
        }
        return render(request, 'form.html', context)


class ReservationsList(View):
    """
    Displays all the reservations sorted by the day when the booking begins.
    """
    @staticmethod
    def get(request):
        reservations = ParkingReservation.objects.all().order_by('from_day')
        context = {
            'reservations': reservations
        }
        return render(request, 'reservations.html', context)


class DeleteReservation(View):
    """
    Allows to delete a specific reservation from db, turns the 'is_free' value back to True.
    """
    @staticmethod
    def get(request, reservation_id):
        reservation = ParkingReservation.objects.get(id=reservation_id)
        context = {
            'reservation': reservation
        }
        return render(request, 'delete_reservation.html', context)

    @staticmethod
    def post(request, reservation_id):
        reservation = ParkingReservation.objects.get(id=reservation_id)
        reservation.parking_place.is_free = True
        reservation.parking_place.save()
        reservation.parking_place.parking.delete_reservation()
        reservation.delete()

        return redirect('/reservation/reservations/')
