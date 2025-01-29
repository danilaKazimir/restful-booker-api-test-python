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


@pytest.fixture
def create_successful_booking(booking_api: BookingApi):
    def _create_successful_booking(missing_field: str = None):
        if missing_field:
            booking_api.create_booking(200, missing_field)
        else:
            booking_api.create_booking(200)

        booking_api.check_successful_create_booking_responses()

        booking_id = booking_api.get_booking_id()

        booking_api.get_booking(booking_id, 200)
        booking_api.check_existing_booking_response()

        booking_api.get_existing_booking_ids(200)
        booking_api.check_get_booking_ids_response(booking_id)

    return _create_successful_booking
