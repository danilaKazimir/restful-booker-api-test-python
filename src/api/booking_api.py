from typing import TypeVar

from pydantic import BaseModel
import allure

from src.base.base_api import BaseApi
from src.models.booking.booking import Booking
from src.models.booking.create_booking_response import CreateBookingResponse
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
        self.__400_RESPONSE_TEXT = 'Bad Request'

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    @allure.step('Send get booking request')
    def get_booking(self, booking_id: int, exp_status_code: int, response_model: PydanticModel):
        url = f'{self.__BOOKING_API_URI}/{booking_id}'
        return self._get(url=url)._check_response_status_code(exp_status_code)._get_response_model(response_model)

    @allure.step('Send get booking ids request')
    def get_existing_booking_ids(self, expected_status_code: int, response_model: PydanticModel) -> PydanticModel:
        return self._get(
            url=self.__BOOKING_API_URI
        )._check_response_status_code(expected_status_code)._get_response_model(response_model)

    @allure.step('Send create booking request')
    def create_booking(self, request: Booking, exp_status_code: int, response_model: PydanticModel):
        return self._post(
            url=self.__BOOKING_API_URI,
            body=request
        )._check_response_status_code(exp_status_code)._get_response_model(response_model)

    @allure.step('Send update booking request')
    def update_booking(self, request: PydanticModel, booking_id: int, expected_status_code: int,
                       response_model: PydanticModel, token: str = None, auth_header: str = None):
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
            body=request,
            headers=headers
        )._check_response_status_code(expected_status_code)._get_response_model(response_model)

    @allure.step('Send delete booking request')
    def delete_booking(self, booking_id: int, expected_status_code: int, response_model: PydanticModel,
                       token: str = None, auth_header: str = None):
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
        )._check_response_status_code(expected_status_code)._get_response_model(response_model)

    @allure.step('Send partial update booking request')
    def partial_update_booking(self, request: PydanticModel, booking_id: int, exp_status_code: int,
                               response_model: PydanticModel, token: str = None, auth_header: str = None):
        headers = {}

        if token:
            headers.update({
                'Cookie': f'token={token}'
            })

        if auth_header:
            headers.update({
                'Authorization': f'Basic {auth_header}'
            })

        return self._patch(
            url=f'{self.__BOOKING_API_URI}/{booking_id}',
            body=request,
            headers=headers
        )._check_response_status_code(exp_status_code)._get_response_model(response_model)

    @staticmethod
    @allure.step('Check successful create booking response')
    def check_successful_create_booking_response(response: CreateBookingResponse, request: Booking) -> None:
        ObjectUtils.check_that_objects_content_are_identical(response.booking, request)

    @staticmethod
    @allure.step('Check existing booking response')
    def check_existing_booking_response(response: Booking, request: Booking) -> None:
        ObjectUtils.check_that_objects_content_are_identical(response, request)

    @allure.step('Check unsuccessful create booking response')
    def check_unsuccessful_create_booking_response(self, response: BookingRootResponse) -> None:
        assert response.root == self.__500_RESPONSE_TEXT, f'Unsuccessful create booking message is incorrect! \
            Expected value - {self.__500_RESPONSE_TEXT}, actual value - {response.root}'

    @allure.step('Check get booking ids response')
    def check_get_booking_ids_response(self, target_id: int, response: BookingIdsResponse) -> None:
        assert any(booking.bookingid == target_id for booking in response.root), f'Booking with \
            {target_id} ID is not found!'

    @allure.step('Check not found booking response')
    def check_not_found_booking_response(self, response: BookingRootResponse) -> None:
        assert response.root == self.__404_RESPONSE_TEXT, f'Booking not found message is incorrect! \
            Expected value - {self.__404_RESPONSE_TEXT}, actual value - {response.root}'

    @allure.step('Check forbidden response')
    def check_forbidden_response(self, response: BookingRootResponse) -> None:
        assert response.root == self.__403_RESPONSE_TEXT, f'Booking forbidden message is incorrect! \
            Expected value - {self.__403_RESPONSE_TEXT}, actual value - {response.root}'

    @allure.step('Check bad request response')
    def check_bad_request_response(self, response: BookingRootResponse) -> None:
        assert response.root == self.__400_RESPONSE_TEXT, f'Booking bad request message is incorrect! \
            Expected value - {self.__400_RESPONSE_TEXT}, actual value - {response.root}'

    @allure.step('Check delete successful response')
    def check_delete_successful_response(self, response: BookingRootResponse) -> None:
        assert response.root == self.__201_RESPONSE_TEXT, f'Booking delete message is incorrect! \
            Expected value - {self.__201_RESPONSE_TEXT}, actual value - {response.root}'

    @allure.step('Check delete unsuccessful response')
    def check_delete_unsuccessful_response(self, response: BookingRootResponse) -> None:
        assert response.root == self.__405_RESPONSE_TEXT, f'Booking delete unsuccessful message is incorrect! \
            Expected value - {self.__405_RESPONSE_TEXT}, actual value - {response.root}'
