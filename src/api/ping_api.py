from typing import TypeVar

from pydantic import BaseModel
import allure

from src.base.base_api import BaseApi
from src.models.health_check.health_check_response import HealthCheckResponse


class PingApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__PING_API_URI = '/ping'
        self.__PING_SUCCESS_MESSAGE = 'Created'

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    @allure.step('Send ping request')
    def ping_request(self, expected_status_code: int) -> PydanticModel:
        return self._get(
            url=self.__PING_API_URI
        )._check_response_status_code(expected_status_code)._get_response_model(HealthCheckResponse)

    @allure.step('Check that ping success message is correct')
    def check_ping_response(self, response: HealthCheckResponse) -> None:
        assert response.root == self.__PING_SUCCESS_MESSAGE, f'Ping success message is incorrect! \
            Expected value - {self.__PING_SUCCESS_MESSAGE}, actual value - {response.root}'
