from tests.conftest import create_successful_booking
from config import AUTH_BASIC_HEADER


class TestUpdateBooking:
    def test_successful_update_with_token(self, create_successful_booking, get_auth_token, booking_api, auth_api):
        create_successful_booking()
        get_auth_token()

        booking_id = booking_api.get_booking_id()
        token = auth_api.get_token()

        booking_api.update_booking(booking_id, 200, token=token)
        booking_api.check_existing_booking_response()

    def test_successful_update_with_auth_header(self, create_successful_booking, get_auth_token, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.update_booking(booking_id, 200, auth_header=AUTH_BASIC_HEADER)
        booking_api.check_existing_booking_response()

    def test_update_without_auth_keys(self, create_successful_booking, get_auth_token, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.update_booking(booking_id, 403)
        booking_api.check_update_forbidden_response()

    def test_update_with_invalid_cookie(self, create_successful_booking, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.update_booking(booking_id, 403, token='invalid_token')
        booking_api.check_update_forbidden_response()

    def test_update_with_invalid_header(self, create_successful_booking, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.update_booking(booking_id, 403, auth_header='invalid_headers')
        booking_api.check_update_forbidden_response()
