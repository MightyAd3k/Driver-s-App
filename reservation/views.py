from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from reservation import models
from reservation.forms import DriverModelForm


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
    template_name = 'form.html'
    success_url = reverse_lazy('drivers')


class DriversList(View):
    def get(self, request):
        drivers = models.Driver.objects.all()
        context = {'drivers': drivers}
        return render(request, 'drivers.html', context)
