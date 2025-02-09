import pytest

from src.api.auth_api import AuthApi
from src.api.ping_api import PingApi
from src.api.booking_api import BookingApi
from config import ADMIN_USERNAME, ADMIN_PASSWORD
from src.models.booking.booking import Booking
from src.models.booking.create_booking_response import CreateBookingResponse
from src.models.create_token.create_token_response import CreateTokenValidResponse


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
def created_booking(booking_api: BookingApi):
    request: Booking = Booking().fill_data()
    response: CreateBookingResponse = booking_api.create_booking(request, 200, CreateBookingResponse)

    yield response.bookingid


@pytest.fixture
def auth_token(auth_api: AuthApi):
    response: CreateTokenValidResponse = auth_api.create_token(ADMIN_USERNAME, ADMIN_PASSWORD, 200,
                                                               CreateTokenValidResponse)

    yield response.token
