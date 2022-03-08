import pytest
from django.http import response
from django.urls import reverse

from reservation.models import Driver


@pytest.mark.django_db
def test_add_driver(client):
    dct = {
        'name': 'Adrian',
        'surname': 'Kainwerd',
        'nationality': 'pl'
    }
    url = reverse('add_driver')
    client.post(url, dct)
    assert Driver.objects.get(**dct)

