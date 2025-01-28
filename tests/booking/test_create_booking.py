import pytest


class TestCreateBooking:
    def test_successful_booking_create(self, booking_api):
        booking_api.create_booking(200)
        booking_api.check_successful_create_booking_responses()

        booking_id = booking_api.get_booking_id()

        booking_api.get_existing_booking(booking_id, 200)
        booking_api.check_existing_booking_response()

    def test_successful_booking_create_without_additional_needs(self, booking_api):
        booking_api.create_booking(200, 'additionalneeds')
        booking_api.check_successful_create_booking_responses()

        booking_id = booking_api.get_booking_id()

        booking_api.get_existing_booking(booking_id, 200)
        booking_api.check_existing_booking_response()

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
