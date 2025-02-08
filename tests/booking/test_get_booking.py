import pytest

from src.models.booking.booking_root_response import BookingRootResponse
from src.models.booking.booking_ids_response import BookingIdsResponse


class TestGetBooking:
    def test_get_booking_after_booking_creation(self, created_booking, booking_api):
        response = booking_api.get_existing_booking_ids(200, BookingIdsResponse)
        booking_api.check_get_booking_ids_response(created_booking, response)

    @pytest.mark.parametrize('booking_id', [999999, 0, -1, 'test'])
    def test_get_not_found_booking(self, booking_api, booking_id):
        response = booking_api.get_booking(booking_id, 404, BookingRootResponse)
        booking_api.check_not_found_booking_response(response)
