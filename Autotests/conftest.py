import pytest


@pytest.fixture()
def requests_users():
    return 'http://localhost:3000/users'


@pytest.fixture()
def requests_department():
    return 'http://localhost:3000/department/'

