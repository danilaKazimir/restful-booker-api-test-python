import pytest

from config import AUTH_BASIC_HEADER


class TestDeleteBooking:
    def test_successful_delete_with_token(self, create_successful_booking, get_auth_token, booking_api, auth_api):
        create_successful_booking()
        get_auth_token()

        booking_id = booking_api.get_booking_id()
        token = auth_api.get_token()

        booking_api.delete_booking(booking_id, 201, token=token)
        booking_api.check_delete_successful_response()

    def test_successful_delete_with_auth_header(self, create_successful_booking, get_auth_token, booking_api):
        create_successful_booking()
        get_auth_token()

        booking_id = booking_api.get_booking_id()

        booking_api.delete_booking(booking_id, 201, auth_header=AUTH_BASIC_HEADER)
        booking_api.check_delete_successful_response()

    def test_delete_without_auth_keys(self, create_successful_booking, get_auth_token, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.delete_booking(booking_id, 403)
        booking_api.check_forbidden_response()

    def test_delete_with_invalid_cookie(self, create_successful_booking, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.delete_booking(booking_id, 403, token='invalid_token')
        booking_api.check_forbidden_response()

    def test_delete_with_invalid_header(self, create_successful_booking, booking_api):
        create_successful_booking()

        booking_id = booking_api.get_booking_id()

        booking_api.delete_booking(booking_id, 403, auth_header='invalid_headers')
        booking_api.check_forbidden_response()

    @pytest.mark.parametrize('booking_id', [999999, 0, -1, 'test'])
    def test_delete_with_invalid_booking_id(self, booking_api, booking_id):
        booking_api.delete_booking(booking_id, 405, auth_header=AUTH_BASIC_HEADER)
        booking_api.check_delete_unsuccessful_response()
