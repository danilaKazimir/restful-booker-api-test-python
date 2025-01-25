from src.base.base_response import BaseResponse
from src.models.create_token.create_token_request import CreateTokenRequest
from src.models.create_token.create_token_response import CreateTokenValidResponse, CreateTokenInvalidResponse


class AuthApi(BaseResponse):
    def __init__(self):
        super().__init__()
        self.__AUTH_API_URI = '/auth'
        self.__INVALID_RESPONSE_TEXT = 'Bad credentials'
        self._token = None

    def create_token(self, username, password, expected_status_code=200):
        request: CreateTokenRequest = CreateTokenRequest()
        request.username = username
        request.password = password

        return self._post(
            url=self.__AUTH_API_URI,
            body=request,
        )._assert_response_status_code(expected_status_code)

    def check_valid_response(self):
        create_token_response: CreateTokenValidResponse = self._get_response_model(CreateTokenValidResponse)
        self._token = create_token_response.token

    def check_invalid_response(self):
        create_token_response: CreateTokenInvalidResponse = self._get_response_model(CreateTokenInvalidResponse)
        assert create_token_response.reason == self.__INVALID_RESPONSE_TEXT, 'Incorrect reason message!'
