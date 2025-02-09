from typing import TypeVar

from pydantic import BaseModel
import allure

from src.base.base_api import BaseApi
from src.models.create_token.create_token_request import CreateTokenRequest
from src.models.create_token.create_token_response import CreateTokenInvalidResponse


class AuthApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__AUTH_API_URI = '/auth'
        self.__INVALID_RESPONSE_REASON_TEXT = 'Bad credentials'

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    @allure.step('Send create token request')
    def create_token(self, username: str, password: str, expected_status_code: int, response_model: PydanticModel) -> PydanticModel:
        request: CreateTokenRequest = CreateTokenRequest(username=username, password=password)

        return self._post(
            url=self.__AUTH_API_URI,
            body=request,
        )._check_response_status_code(expected_status_code)._get_response_model(response_model)

    @allure.step('Check that reason field is correct')
    def check_invalid_response(self, response: CreateTokenInvalidResponse) -> None:
        assert response.reason == self.__INVALID_RESPONSE_REASON_TEXT, f'Invalid response reason is incorrect! \
            Expected value - {self.__INVALID_RESPONSE_REASON_TEXT}, actual value - {response.reason}'
