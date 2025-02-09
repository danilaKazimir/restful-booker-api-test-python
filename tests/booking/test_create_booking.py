import pytest
import allure

from src.models.booking.booking import Booking
from src.models.booking.booking_root_response import BookingRootResponse
from src.models.booking.create_booking_response import CreateBookingResponse


class TestCreateBooking:
    @pytest.mark.parametrize('missing_field', [None, 'additionalneeds'])
    @allure.feature('Booking API')
    @allure.story('Create booking')
    @allure.title('Create new booking')
    @allure.description('Check that booking is successfully created')
    def test_successful_booking_create(self, booking_api, missing_field):
        create_booking_request = Booking().fill_data()
        if missing_field:
            setattr(create_booking_request, missing_field, None)

        create_booking_response: CreateBookingResponse = booking_api.create_booking(
            create_booking_request, 200, CreateBookingResponse)
        booking_api.check_successful_create_booking_response(create_booking_response, create_booking_request)

        booking_id = create_booking_response.bookingid

        get_booking_response = booking_api.get_booking(booking_id, 200, Booking)
        booking_api.check_existing_booking_response(get_booking_response, create_booking_request)

    @pytest.mark.parametrize('missing_field', [
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'checkin',
        'checkout'
    ])
    @allure.feature('Booking API')
    @allure.story('Create booking')
    @allure.title('Check required field in creation request')
    @allure.description('Check that booking is not created, if required field is missing')
    def test_create_booking_with_missing_required_field(self, booking_api, missing_field):
        request = Booking().fill_data()
        if missing_field and missing_field not in ['checkin', 'checkout']:
            setattr(request, missing_field, None)
        elif missing_field and missing_field in ['checkin', 'checkout']:
            setattr(request.bookingdates, missing_field, None)

        response = booking_api.create_booking(request, 500, BookingRootResponse)
        booking_api.check_unsuccessful_create_booking_response(response)
