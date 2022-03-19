import pytest
from django.urls import reverse

from reservation.models import Driver, Parking, Vehicle, ParkingReservation

""" >>>>>>> Driver test <<<<<<< """


@pytest.mark.django_db
def test_driver_create_view(client, driver):
    dct = {
        'name': 'Janusz',
        'surname': 'Drew',
        'nationality': 'pl',
        'user': driver.id
    }
    url = reverse('add_driver')
    client.post(url, dct)
    assert Driver.objects.get(**dct)


@pytest.mark.django_db
def test_driver_detail_view(client, driver):
    url = reverse('detail_driver', args=(driver.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_driver_update_view(client, driver):
    url = reverse('update_driver', args=(driver.id,))
    dct = {
        'name': 'Martyna',
        'surname': 'Drew',
        'nationality': 'de',
        'user': driver.id
    }
    response = client.post(url, dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_delete_view(client, driver):
    url = reverse('delete_driver', args=(driver.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_drivers_list_view(client, drivers):
    url = reverse('drivers')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['drivers'].count() == len(drivers)
    for item in drivers:
        assert item in context['drivers']


""" >>>>>>>> Parking tests <<<<<<<< """


@pytest.mark.django_db
def test_parking_create_view(client, parking):
    dct = {
        'address': 'Gliwicka 44',
        'type': 'trucks',
        'number_of_places': 25,
        'free_places': 25
    }
    url = reverse('add_parking')
    client.post(url, dct)
    assert Parking.objects.get(**dct)


@pytest.mark.django_db
def test_parking_detail_view(client, parking):
    url = reverse('detail_parking', args=(parking.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_parking_update_view(client, parking):
    url = reverse('update_parking', args=(parking.id,))
    dct = {
        'address': 'Złota 44',
        'type': 'cars',
        'number_of_places': 2137,
        'free_places': 2137
    }
    response = client.post(url, dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_parking_delete_view(client, parking):
    url = reverse('delete_parking', args=(parking.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_parkings_list_view(client, parkings):
    url = reverse('parkings')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['parkings'].count() == len(parkings)
    for item in parkings:
        assert item in context['parkings']


""" >>>>>>>>> Vehicle tests <<<<<<<<< """


@pytest.mark.django_db
def test_vehicle_create_view(client, vehicle, driver):
    dct = {
        'type': 'truck',
        'license_plate': 'SZY16914',
        'driver_name': driver.id,
    }
    url = reverse('add_vehicle')
    response = client.post(url, dct)
    assert Vehicle.objects.get(**dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_vehicle_detail_view(client, vehicle):
    url = reverse('detail_vehicle', args=(vehicle.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vehicle_update_view(client, vehicle, driver):
    url = reverse('update_vehicle', args=(vehicle.id,))
    dct = {
        'type': 'car',
        'license_plate': 'SK54ZX25',
        'driver_name': driver.id,
    }
    response = client.post(url, dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_vehicle_delete_view(client, vehicle):
    url = reverse('detail_vehicle', args=(vehicle.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vehicle_list_view(client, vehicles):
    url = reverse('vehicles')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['vehicles'].count() == len(vehicles)
    for item in vehicles:
        assert item in context['vehicles']


""" >>>>>>>>>> Reservation tests <<<<<<<<<< """


@pytest.mark.django_db
def test_reservation_create_view(client, reservation, driver, parking_place, parking):
    dct = {
        'from_day': '2022-03-11',
        'from_hour': '10:00',
        'to_day': '2022-03-12',
        'to_hour': '11:00',
        'driver': driver.id,
        'parking_place': parking_place.id
    }
    url = reverse('add_reservation', args=(parking.id,))
    response = client.post(url, dct)
    assert ParkingReservation.objects.get(**dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_reservation_detail_view(client, reservation):
    url = reverse('detail_reservation', args=(reservation.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_reservation_update_view(client, reservation, driver, parking_place):
    dct = {
        'from_day': '2022-03-11',
        'from_hour': '22:00',
        'to_day': '2035-03-11',
        'to_hour': '00:00',
        'driver': driver.id,
        'parking_place': parking_place.id
    }
    url = reverse('update_reservation', args=(reservation.id,))
    response = client.post(url, dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_reservation_delete_view(client, reservation):
    url = reverse('delete_reservation', args=(reservation.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vehicle_list_view(client, reservations):
    url = reverse('reservations')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['reservations'].count() == len(reservations)
    for item in reservations:
        assert item in context['vehicles']
