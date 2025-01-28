from src.base.base_api import BaseApi
from src.models.health_check.health_check_response import HealthCheckResponse


class PingApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__AUTH_API_URI = '/ping'
        self.__PING_SUCCESS_MESSAGE = 'Created'

    def ping_request(self, expected_status_code: int) -> None:
        return self._get(url=self.__AUTH_API_URI)._check_response_status_code(expected_status_code)

    def check_ping_response(self) -> None:
        self._get_response_model(HealthCheckResponse)
        self._check_response_field_value('root', self.__PING_SUCCESS_MESSAGE)
