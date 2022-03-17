import pytest
from django.contrib.auth.models import User

from django.test import Client as WebClient

from reservation.models import Driver, Parking


@pytest.fixture
def client():
    client = WebClient()
    return client


@pytest.fixture
def new_user():
    user = User.objects.create(username='Janusz')
    user.set_password('silneHaslo!2')
    user.save()
    return user


@pytest.fixture
def new_driver(new_user):
    driver = Driver.objects.create(name='Janusz', surname='Drew', nationality='pl', user=new_user)
    return driver


@pytest.fixture
def new_parking():
    parking = Parking.objects.create(address='Gliwicka 44', type='trucks', number_of_places=25, free_places=25)
    return parking