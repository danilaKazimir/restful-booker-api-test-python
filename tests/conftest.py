import pytest

from src.api.auth_api import AuthApi
from src.api.ping_api import PingApi
from src.api.booking_api import BookingApi


@pytest.fixture
def auth_api() -> AuthApi:
    return AuthApi()


@pytest.fixture
def ping_api() -> PingApi:
    return PingApi()


@pytest.fixture
def booking_api() -> BookingApi:
    return BookingApi()
