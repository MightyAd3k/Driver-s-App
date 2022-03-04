from unittest import TestCase

import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_login(client, new_user):
    url = reverse('login')
    dct = {
        'username': 'Janusz',
        'password': 'asd123'
    }
    response = client.post(url, dct)
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_logout(client, new_user):
    url = reverse('logout')
    dct = {
        'username': 'Janusz',
        'password': 'asd123'
    }
    response = client.post(url, dct)
    assert not response.wsgi_request.user.is_authenticated


# @pytest.mark.django_db
# def test_user_registration(client):
    # dct = {
    #     'password': 'asd123AS!@',
    #     'last_login': '2022-03-04 13:56:36.671752 +00:00',
    #     'is_superuser': False,
    #     'username': 'Janek18',
    #     'first_name': 'Zofia',
    #     'last_name': 'Steczkowska',
    #     'email': 'powodzenia12@wp.pl',
    #     'is_staff': True,
    #     'is_active': False,
    #     'date_joined': '2022-03-02 16:18:33.640584 +00:00'
    #
    # }
    # dct = {
    #     'username': 'Ad3k',
    #     'password': 'strongpass',
    # }
    # url = reverse('register_new_user')
    # client.post(url, dct)
    # assert User.objects.get(**dct)

