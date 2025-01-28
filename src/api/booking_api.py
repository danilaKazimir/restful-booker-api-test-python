from src.base.base_api import BaseApi
from src.models.booking.booking import Booking
from src.models.booking.create_booking_request import CreateBookingRequest
from src.models.booking.create_booking_response import CreateBookingValidResponse, CreateBookingInvalidResponse
from src.utils.object_utils import ObjectUtils


class BookingApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__AUTH_API_URI = '/booking'
        self.__CREATE_API_ERROR_TEXT = 'Internal Server Error'
        self.__FULL_RESPONSE_ATTRIBUTES = (
            'firstname',
            'lastname',
            'totalprice',
            'depositpaid',
            'bookingdates.checkin',
            'bookingdates.checkout',
            'additionalneeds',
        )

    def create_booking(self, expected_status_code: int, missing_field: str = None) -> None:
        self._request = CreateBookingRequest()
        if missing_field:
            ObjectUtils.set_attr(self._request, missing_field, None)

        return self._post(
            url=self.__AUTH_API_URI,
            body=self._request,
        )._check_response_status_code(expected_status_code)

    def get_existing_booking(self, booking_id: int, expected_status_code: int):
        URL = f'{self.__AUTH_API_URI}/{booking_id}'
        return self._get(url=URL)._check_response_status_code(expected_status_code)

    def get_booking_id(self):
        return self._response_model.bookingid

    def check_successful_create_booking_responses(self):
        self._get_response_model(CreateBookingValidResponse)
        self.__check_attributes()

    def check_existing_booking_response(self):
        self._get_response_model(Booking)
        self.__check_attributes()

    def check_unsuccessful_create_booking_response(self):
        self._get_response_model(CreateBookingInvalidResponse)
        self._check_response_field_value('root', self.__CREATE_API_ERROR_TEXT)

    def __check_request_and_response_attribute_value_equals(self, attribute):
        actual_value = ObjectUtils.get_attr(self._request, attribute)
        try:
            expected_value = ObjectUtils.get_attr(self._response_model, attribute)
        except AttributeError:
            expected_value = ObjectUtils.get_attr(self._response_model, f'booking.{attribute}')

        assert actual_value == expected_value, f'{attribute} attribute value from request and response' \
            f'isn\'t equals! Expected value - {expected_value}, actual value - {actual_value}.'

    def __check_attributes(self, attributes=None):
        if attributes is None:
            attributes = self.__FULL_RESPONSE_ATTRIBUTES

        for attribute in attributes:
            self.__check_request_and_response_attribute_value_equals(attribute)
