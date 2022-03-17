import pytest
from django.urls import reverse

from reservation.models import Driver, Parking


@pytest.mark.django_db
def test_add_driver(client, new_driver):
    dct = {
        'name': 'Janusz',
        'surname': 'Drew',
        'nationality': 'pl',
        'user': new_driver.id
    }
    url = reverse('add_driver')
    client.post(url, dct)
    assert Driver.objects.get(**dct)


@pytest.mark.django_db
def test_add_parking(client, new_parking):
    dct = {
        'address': 'Gliwicka 44',
        'type': 'trucks',
        'number_of_places': 25,
        'free_places': 25
    }
    url = reverse('add_parking')
    client.post(url, dct)
    assert Parking.objects.get(**dct)
