import pytest
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
