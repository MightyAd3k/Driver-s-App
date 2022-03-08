import pytest

from django.test import Client as WebClient


@pytest.fixture
def client():
    client = WebClient()
    return client
