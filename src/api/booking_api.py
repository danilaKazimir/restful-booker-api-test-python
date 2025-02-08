from src.base.base_api import BaseApi
from src.models.booking.booking import Booking
from src.models.booking.create_booking_request import CreateBookingRequest
from src.models.booking.create_booking_response import CreateBookingValidResponse
from src.models.booking.booking_ids_response import BookingIdsResponse
from src.models.booking.booking_root_response import BookingRootResponse
from src.utils.object_utils import ObjectUtils


class BookingApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__BOOKING_API_URI = '/booking'
        self.__500_RESPONSE_TEXT = 'Internal Server Error'
        self.__404_RESPONSE_TEXT = 'Not Found'
        self.__403_RESPONSE_TEXT = 'Forbidden'
        self.__201_RESPONSE_TEXT = 'Created'
        self.__405_RESPONSE_TEXT = 'Method Not Allowed'
        self.__FULL_RESPONSE_ATTRIBUTES = (
            'firstname',
            'lastname',
            'totalprice',
            'depositpaid',
            'bookingdates.checkin',
            'bookingdates.checkout',
            'additionalneeds',
        )
        self.__booking_id = None

    def create_booking(self, expected_status_code: int, missing_field: str = None) -> None:
        self._request = CreateBookingRequest()
        if missing_field:
            ObjectUtils.set_attr(self._request, missing_field, None)

        return self._post(
            url=self.__BOOKING_API_URI,
            body=self._request,
        )._check_response_status_code(expected_status_code)

    def update_booking(self, booking_id: int, expected_status_code: int, token: str = None, auth_header: str = None,
                       missing_field: str = None):
        self._request = CreateBookingRequest()
        if missing_field:
            ObjectUtils.set_attr(self._request, missing_field, None)

        headers = {}

        if token:
            headers.update({
                'Cookie': f'token={token}'
            })

        if auth_header:
            headers.update({
                'Authorization': f'Basic {auth_header}'
            })

        return self._put(
            url=f'{self.__BOOKING_API_URI}/{booking_id}',
            body=self._request,
            headers=headers
        )._check_response_status_code(expected_status_code)

    def delete_booking(self, booking_id: int, expected_status_code: int, token: str = None, auth_header: str = None):
        headers = {}

        if token:
            headers.update({
                'Cookie': f'token={token}'
            })

        if auth_header:
            headers.update({
                'Authorization': f'Basic {auth_header}'
            })

        return self._delete(
            url=f'{self.__BOOKING_API_URI}/{booking_id}',
            headers=headers
        )._check_response_status_code(expected_status_code)

    def get_booking(self, booking_id: int, expected_status_code: int) -> None:
        URL = f'{self.__BOOKING_API_URI}/{booking_id}'
        return self._get(url=URL)._check_response_status_code(expected_status_code)

    def get_existing_booking_ids(self, expected_status_code: int) -> None:
        return self._get(url=self.__BOOKING_API_URI)._check_response_status_code(expected_status_code)

    def get_booking_id(self) -> int:
        return self.__booking_id

    def check_successful_create_booking_responses(self) -> None:
        self._get_response_model(CreateBookingValidResponse)
        self.__booking_id = self._response_model.bookingid
        self.__check_attributes()

    def check_existing_booking_response(self) -> None:
        self._get_response_model(Booking)
        self.__check_attributes()

    def check_unsuccessful_create_booking_response(self) -> None:
        self._get_response_model(BookingRootResponse)
        self._check_response_field_value(
            'root',
            self.__500_RESPONSE_TEXT,
            'Unsuccessful create booking message is incorrect!',
        )

    def check_get_booking_ids_response(self, booking_id: int) -> None:
        self._get_response_model(BookingIdsResponse)
        self.__check_if_needed_id_is_exist(booking_id)

    def check_not_found_booking_response(self) -> None:
        self._get_response_model(BookingRootResponse)
        self._check_response_field_value(
            'root',
            self.__404_RESPONSE_TEXT,
            'Booking not found message is incorrect!',
        )

    def check_forbidden_response(self) -> None:
        self._get_response_model(BookingRootResponse)
        self._check_response_field_value(
            'root',
            self.__403_RESPONSE_TEXT,
            'Booking forbidden message is incorrect!'
        )

    def check_delete_successful_response(self) -> None:
        self._get_response_model(BookingRootResponse)
        self._check_response_field_value(
            'root',
            self.__201_RESPONSE_TEXT,
            'Booking delete message is incorrect!'
        )

    def check_delete_unsuccessful_response(self) -> None:
        self._get_response_model(BookingRootResponse)
        self._check_response_field_value(
            'root',
            self.__405_RESPONSE_TEXT,
            'Booking delete unsuccessful message is incorrect!'
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
