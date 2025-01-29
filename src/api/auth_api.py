from src.base.base_api import BaseApi
from src.models.create_token.create_token_request import CreateTokenRequest
from src.models.create_token.create_token_response import CreateTokenValidResponse, CreateTokenInvalidResponse


class AuthApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__AUTH_API_URI = '/auth'
        self.__INVALID_RESPONSE_REASON = 'Bad credentials'
        self._token = None

    def create_token(self, username: str, password: str, expected_status_code: int) -> None:
        request: CreateTokenRequest = CreateTokenRequest(username=username, password=password)

        return self._post(
            url=self.__AUTH_API_URI,
            body=request,
        )._check_response_status_code(expected_status_code)

    def check_valid_response(self) -> None:
        self._get_response_model(CreateTokenValidResponse)
        self._token = self._response_model.token

    def check_invalid_response(self) -> None:
        self._get_response_model(CreateTokenInvalidResponse)
        self._check_response_field_value(
            'reason',
            self.__INVALID_RESPONSE_REASON,
            'Invalid response reason is incorrect!',
        )
