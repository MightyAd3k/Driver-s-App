import random

from faker import Faker
import pytest
from django.contrib.auth.models import User

from django.test import Client as WebClient

from reservation.models import Driver, Parking, nationalities, parking_types, Vehicle, vehicle_types, ParkingPlace, \
    ParkingReservation

faker = Faker('pl_PL')


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
def users():
    lst = []
    for user in range(10):
        lst.append((User.objects.create(username=faker.name(), password='silneHaslo!2')))
    return lst


@pytest.fixture
def driver(new_user):
    driver = Driver.objects.create(name='Janusz', surname='Drew', nationality='pl', user=new_user)
    return driver


@pytest.fixture
def drivers():
    lst = []
    for user in User.objects.all():
        lst.append(Driver.objects.create(name=faker.name(), surname=faker.name(),
                                         nationality=random.choice(nationalities), user=user))
    return lst


@pytest.fixture
def parking():
    parking = Parking.objects.create(address='Gliwicka 44', type='trucks', number_of_places=25, free_places=25)
    return parking


@pytest.fixture
def parkings():
    lst = []
    for parking in range(10):
        lst.append(Parking.objects.create(address=faker.address(), type=random.choice(parking_types),
                                          number_of_places=random.randint(0, 50), free_places=random.randint(0, 50)))
    return lst


@pytest.fixture
def vehicle(driver):
    vehicle = Vehicle.objects.create(type='truck', license_plate='SZY16914', driver_name=driver)
    return vehicle


@pytest.fixture
def vehicles():
    lst = []
    for driver in Driver.objects.all():
        lst.append(Vehicle.objects.create(type=random.choice(vehicle_types),
                                          license_plate=faker.license_plate(),
                                          driver_name=driver))
    return lst


@pytest.fixture
def parking_place(parking):
    parking_place = ParkingPlace.objects.create(parking=parking, is_free=True)
    return parking_place


@pytest.fixture
def parking_places():
    lst = []
    for parking in Parking.objects.all():
        lst.append(ParkingPlace.objects.create(parking=parking, is_free=True))
    return lst


@pytest.fixture
def reservation(driver, parking_place):
    reservation = ParkingReservation.objects.create(from_day='2022-03-11', from_hour='10:00',
                                                    to_day='2022-03-12', to_hour='11:00',
                                                    driver=driver, parking_place=parking_place)
    return reservation


@pytest.fixture
def reservations():
    lst = []
    for driver in Driver.objects.all():
        for parking_place in ParkingPlace.objects.all():
            lst.append(ParkingReservation.objects.create(from_day='2022-03-11', from_hour='10:00',
                                                         to_day='2022-03-12', to_hour='11:00',
                                                         driver=driver, parking_place=parking_place))
    return lst
