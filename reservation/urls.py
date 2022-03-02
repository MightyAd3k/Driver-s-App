from django.urls import path

from reservation import views

urlpatterns = [
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
