from src.base.base_response import BaseResponse
from src.models.health_check.health_check_response import HealthCheckResponse


class PingApi(BaseResponse):
    def __init__(self):
        super().__init__()
        self.__AUTH_API_URI = '/ping'
        self.__PING_SUCCESS_MESSAGE = 'Created'

    def ping_request(self):
        return self._get(
            url=self.__AUTH_API_URI,
        )._assert_response_status_code(201)

    def check_ping_response(self):
        ping_response: HealthCheckResponse = self._get_response_model(HealthCheckResponse)
        assert ping_response.root == self.__PING_SUCCESS_MESSAGE, 'Incorrect ping message!'
