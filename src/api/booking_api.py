from src.base.base_api import BaseApi
from src.models.booking.booking import Booking
from src.models.booking.create_booking_request import CreateBookingRequest
from src.models.booking.create_booking_response import CreateBookingValidResponse, CreateBookingInvalidResponse
from src.models.booking.booking_ids_response import BookingIdsResponse
from src.models.booking.get_booking_not_found_response import GetBookingNotFoundResponse
from src.utils.object_utils import ObjectUtils


class BookingApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__BOOKING_API_URI = '/booking'
        self.__CREATE_API_ERROR_TEXT = 'Internal Server Error'
        self.__BOOKING_NOT_FOUND_RESPONSE = 'Not Found'
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
            url=self.__BOOKING_API_URI,
            body=self._request,
        )._check_response_status_code(expected_status_code)

    def get_booking(self, booking_id: int, expected_status_code: int) -> None:
        URL = f'{self.__BOOKING_API_URI}/{booking_id}'
        return self._get(url=URL)._check_response_status_code(expected_status_code)

    def get_existing_booking_ids(self, expected_status_code: int) -> None:
        return self._get(url=self.__BOOKING_API_URI)._check_response_status_code(expected_status_code)

    def get_booking_id(self) -> int:
        return self._response_model.bookingid

    def check_successful_create_booking_responses(self) -> None:
        self._get_response_model(CreateBookingValidResponse)
        self.__check_attributes()

    def check_existing_booking_response(self) -> None:
        self._get_response_model(Booking)
        self.__check_attributes()

    def check_unsuccessful_create_booking_response(self) -> None:
        self._get_response_model(CreateBookingInvalidResponse)
        self._check_response_field_value(
            'root',
            self.__CREATE_API_ERROR_TEXT,
            'Unsuccessful create booking message is incorrect!',
        )

    def check_get_booking_ids_response(self, booking_id: int) -> None:
        self._get_response_model(BookingIdsResponse)
        self.__check_if_needed_id_is_exist(booking_id)

    def check_not_found_booking_response(self) -> None:
        self._get_response_model(GetBookingNotFoundResponse)
        self._check_response_field_value(
            'root',
            self.__BOOKING_NOT_FOUND_RESPONSE,
            'Booking not found message is incorrect!',
        )

    def __check_request_and_response_attribute_value_equals(self, attribute: str) -> None:
        actual_value = ObjectUtils.get_attr(self._request, attribute)
        try:
            expected_value = ObjectUtils.get_attr(self._response_model, attribute)
        except AttributeError:
            expected_value = ObjectUtils.get_attr(self._response_model, f'booking.{attribute}')

        assert actual_value == expected_value, f'{attribute} attribute value from request and response' \
            f'isn\'t equals! Expected value - {expected_value}, actual value - {actual_value}.'

    def __check_attributes(self, attributes=None) -> None:
        if attributes is None:
            attributes = self.__FULL_RESPONSE_ATTRIBUTES

        for attribute in attributes:
            self.__check_request_and_response_attribute_value_equals(attribute)

    def __check_if_needed_id_is_exist(self, target_id: int) -> None:
        assert any(booking.bookingid == target_id for booking in self._response_model.root), f'' \
            f'Booking with ID {target_id} is not found!'
