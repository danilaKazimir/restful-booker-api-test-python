import pytest

from config import AUTH_BASIC_HEADER
from src.models.booking.booking import Booking
from src.utils.object_utils import ObjectUtils


class TestPartialUpdateBooking:
    @pytest.mark.parametrize('updated_field', [
        ['firstname'],
        ['lastname'],
        ['totalprice'],
        ['depositpaid'],
        ['additionalneeds'],
        ['firstname', 'lastname'],
        ['totalprice', 'depositpaid'],
        ['checkin', 'checkout'],
        ['firstname', 'lastname', 'totalprice'],
        ['depositpaid', 'checkin', 'checkout', 'additionalneeds'],
        ['firstname', 'lastname', 'totalprice', 'depositpaid', 'additionalneeds'],
        ['firstname', 'lastname', 'totalprice', 'depositpaid', 'checkin', 'checkout', 'additionalneeds']
    ], ids=[
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'additionalneeds',
        'firstname, lastname',
        'totalprice, depositpaid',
        'checkin, checkout',
        'firstname, lastname, totalprice',
        'depositpaid, checkin, checkout, additionalneeds',
        'firstname, lastname, totalprice, depositpaid, additionalneeds',
        'firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds'
    ])
    def test_partial_update_with_token(self, booking_api, updated_field, created_booking, auth_token):
        original_booking_values = booking_api.get_booking(created_booking, 200, Booking)

        update_request = Booking().fill_data(full_data=False, fields=list(updated_field))

        booking_values_after_update = ObjectUtils.deep_update_model(original_booking_values, update_request)
        # TODO add tests for only checkin or checkout fields

        update_response = booking_api.partial_update_booking(
            update_request, created_booking, 200, Booking, token=auth_token)

        booking_api.check_existing_booking_response(update_response, booking_values_after_update)

    @pytest.mark.parametrize('updated_field', [
        ['firstname'],
        ['lastname'],
        ['totalprice'],
        ['depositpaid'],
        ['additionalneeds'],
        ['firstname', 'lastname'],
        ['totalprice', 'depositpaid'],
        ['checkin', 'checkout'],
        ['firstname', 'lastname', 'totalprice'],
        ['depositpaid', 'checkin', 'checkout', 'additionalneeds'],
        ['firstname', 'lastname', 'totalprice', 'depositpaid', 'additionalneeds'],
        ['firstname', 'lastname', 'totalprice', 'depositpaid', 'checkin', 'checkout', 'additionalneeds']
    ], ids=[
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'additionalneeds',
        'firstname, lastname',
        'totalprice, depositpaid',
        'checkin, checkout',
        'firstname, lastname, totalprice',
        'depositpaid, checkin, checkout, additionalneeds',
        'firstname, lastname, totalprice, depositpaid, additionalneeds',
        'firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds'
    ])
    def test_partial_update_with_auth_header(self, booking_api, created_booking, updated_field):
        original_booking_values = booking_api.get_booking(created_booking, 200, Booking)

        update_request = Booking().fill_data(full_data=False, fields=list(updated_field))

        booking_values_after_update = ObjectUtils.deep_update_model(original_booking_values, update_request)
        # TODO add tests for only checkin or checkout fields

        update_response = booking_api.partial_update_booking(
            update_request, created_booking, 200, Booking, auth_header=AUTH_BASIC_HEADER)

        booking_api.check_existing_booking_response(update_response, booking_values_after_update)
