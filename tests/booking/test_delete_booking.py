import pytest

from config import AUTH_BASIC_HEADER
from src.models.booking.booking_root_response import BookingRootResponse


class TestDeleteBooking:
    def test_successful_delete_with_token(self, created_booking, auth_token, booking_api):
        response = booking_api.delete_booking(created_booking, 201, BookingRootResponse, token=auth_token)
        booking_api.check_delete_successful_response(response)

        get_response = booking_api.get_booking(created_booking, 404, BookingRootResponse)
        booking_api.check_not_found_booking_response(get_response)

    def test_successful_delete_with_auth_header(self, created_booking, booking_api):
        response = booking_api.delete_booking(created_booking, 201, BookingRootResponse, auth_header=AUTH_BASIC_HEADER)
        booking_api.check_delete_successful_response(response)

        get_response = booking_api.get_booking(created_booking, 404, BookingRootResponse)
        booking_api.check_not_found_booking_response(get_response)

    def test_delete_without_auth_keys(self, created_booking, booking_api):
        response = booking_api.delete_booking(created_booking, 403, BookingRootResponse)
        booking_api.check_forbidden_response(response)

    def test_delete_with_invalid_cookie(self, created_booking, booking_api):
        response = booking_api.delete_booking(created_booking, 403, BookingRootResponse, token='invalid_token')
        booking_api.check_forbidden_response(response)

    def test_delete_with_invalid_header(self, created_booking, booking_api):
        response = booking_api.delete_booking(created_booking, 403, BookingRootResponse, auth_header='invalid_headers')
        booking_api.check_forbidden_response(response)

    @pytest.mark.parametrize('booking_id', [999999, 0, -1, 'test'])
    def test_delete_non_existent_booking(self, booking_api, booking_id):
        response = booking_api.delete_booking(booking_id, 405, BookingRootResponse, auth_header=AUTH_BASIC_HEADER)
        booking_api.check_delete_unsuccessful_response(response)
