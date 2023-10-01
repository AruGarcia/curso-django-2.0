import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('turma:indice'))


def status_code(resp):
    assert resp.status_code == 200
