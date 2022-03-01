"""FinishProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    # Drvier urls
    path('add_driver/', views.AddDriver.as_view(), name='add_driver'),
    path('driver/<int:pk>/', views.DetailsDriver.as_view(), name='detail_driver'),
    path('driver/<int:pk>/update/', views.UpdateDriver.as_view(), name='update'),
    path('driver/<int:pk>/delete/', views.DeleteDriver.as_view(), name='delete'),
    path('drivers/', views.DriversList.as_view(), name='drivers'),
    # Vehicle urls
    path('add_vehicle/', views.AddVehicle.as_view(), name='add_vehicle'),
    path('vehicles/', views.VehiclesList.as_view(), name='vehicles'),
    path('vehicle/<int:pk>/', views.DetailsVehicle.as_view(), name='detail_vehicle'),
    path('vehicle/<int:pk>/update/', views.UpdateVehicle.as_view(), name='update'),
    path('vehicle/<int:pk>/delete/', views.DeleteVehicle.as_view(), name='delete'),
]
