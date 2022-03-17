import pytest as pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient


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
