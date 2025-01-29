import pytest


class TestGetBookingInvalid:
    @pytest.mark.parametrize('booking_id', [999999, 0, -1, 'test'])
    def test_get_not_found_booking(self, booking_api, booking_id):
        booking_api.get_booking(booking_id, 404)
        booking_api.check_not_found_booking_response()
