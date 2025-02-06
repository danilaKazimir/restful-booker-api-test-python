import pytest

from tests.conftest import create_successful_booking


class TestCreateBooking:
    @pytest.mark.parametrize('missing_field', [None, 'additionalneeds'])
    def test_successful_booking_create(self, create_successful_booking, missing_field):
        create_successful_booking(missing_field)

    @pytest.mark.parametrize('missing_field', [
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'bookingdates.checkin',
        'bookingdates.checkout'
    ])
    def test_unsuccessful_booking_create(self, booking_api, missing_field):
        booking_api.create_booking(500, missing_field)
        booking_api.check_unsuccessful_create_booking_response()
