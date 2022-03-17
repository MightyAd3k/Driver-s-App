from unittest import TestCase

import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_login(client, new_user):
    url = reverse('login')
    dct = {
        'username': 'Janusz',
        'password': 'silneHaslo!2'
    }
    response = client.post(url, dct)
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_logout(client, new_user):
    url = reverse('logout')
    dct = {
        'username': 'Janusz',
        'password': 'silneHaslo!2'
    }
    response = client.post(url, dct)
    assert not response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_user_registration(client):
    dct = {
        'username': 'Ad3k',
        'password': 'strongpaSs*9',
        'password1': 'strongpaSs*9',
    }
    url = reverse('register_new_user')
    client.post(url, dct)
    assert User.objects.get(username=dct['username'])
