import pytest
from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

@pytest.fixture

def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user():
    client = TestClient(app)
    resource = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret'
        },
    )
    assert resource.status_code == HTTPStatus.CREATED
    assert resource.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
