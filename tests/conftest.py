import pytest

from src.api.auth_api import AuthApi
from src.api.ping_api import PingApi


@pytest.fixture
def auth_api():
    return AuthApi()


@pytest.fixture
def ping_api():
    return PingApi()
