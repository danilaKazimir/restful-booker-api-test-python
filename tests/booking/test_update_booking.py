import pytest
import allure

from config import AUTH_BASIC_HEADER
from src.models.booking.booking_root_response import BookingRootResponse
from src.models.booking.booking import Booking


class TestUpdateBooking:
    @allure.feature('Booking API')
    @allure.story('Full update booking')
    @allure.title('Update existing booking with authentication token')
    @allure.description('Check that booking is successfully updated (with authentication token)')
    def test_successful_update_with_token(self, created_booking, auth_token, booking_api):
        request = Booking().fill_data()
        # TODO add test with put request without additionalneeds
        # if missing_field:
        #     setattr(request, missing_field, None)

        response = booking_api.update_booking(request, created_booking, 200, Booking, token=auth_token)
        booking_api.check_existing_booking_response(response, request)

    @allure.feature('Booking API')
    @allure.story('Full update booking')
    @allure.title('Update existing booking with authentication basic header')
    @allure.description('Check that booking is successfully updated (with authentication basic header)')
    def test_successful_update_with_auth_header(self, created_booking, booking_api):
        request = Booking().fill_data()
        # TODO add test with put request without additionalneeds
        # if missing_filed:
        #     setattr(request, missing_filed, None)

        response = booking_api.update_booking(request, created_booking, 200, Booking, auth_header=AUTH_BASIC_HEADER)

        booking_api.check_existing_booking_response(response, request)

    @allure.feature('Booking API')
    @allure.story('Full update booking')
    @allure.title('Update booking without authentication keys')
    @allure.description('Check that booking is not updated if no authentication keys is used')
    def test_update_without_auth_keys(self, created_booking, booking_api):
        request = Booking().fill_data()
        response = booking_api.update_booking(request, created_booking, 403, BookingRootResponse)
        booking_api.check_forbidden_response(response)

    @allure.feature('Booking API')
    @allure.story('Full update booking')
    @allure.title('Update booking with invalid authentication token')
    @allure.description('Check that booking is not updated if authentication token is invalid')
    def test_update_with_invalid_token(self, created_booking, booking_api):
        request = Booking().fill_data()
        response = booking_api.update_booking(request, created_booking, 403, BookingRootResponse, token='invalid_token')
        booking_api.check_forbidden_response(response)

    @allure.feature('Booking API')
    @allure.story('Full update booking')
    @allure.title('Update booking with invalid authentication basic header')
    @allure.description('Check that booking is not updated if authentication basic header is invalid')
    def test_update_with_invalid_header(self, created_booking, booking_api):
        request = Booking().fill_data()
        response = booking_api.update_booking(request, created_booking, 403, BookingRootResponse,
                                              auth_header='invalid_header')
        booking_api.check_forbidden_response(response)

    @allure.feature('Booking API')
    @allure.story('Full update booking')
    @allure.title('Check required field in full update request')
    @allure.description('Check that booking is not updated, if required field is missing')
    @pytest.mark.parametrize('missing_field', [
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'checkin',
        'checkout'
    ])
    def test_update_without_needed_field(self, created_booking, booking_api, auth_api, missing_field):
        request = Booking().fill_data()
        if missing_field and missing_field not in ['checkin', 'checkout']:
            setattr(request, missing_field, None)
        elif missing_field and missing_field in ['checkin', 'checkout']:
            setattr(request.bookingdates, missing_field, None)

        response = booking_api.update_booking(request, created_booking, 400, BookingRootResponse,
                                              auth_header=AUTH_BASIC_HEADER)
        booking_api.check_bad_request_response(response)
