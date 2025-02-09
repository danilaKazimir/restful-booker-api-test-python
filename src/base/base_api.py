from typing import TypeVar, Mapping

import requests
from requests import Response
from pydantic import BaseModel, ValidationError
from requests import JSONDecodeError

from config import BASE_URL


class BaseApi:
    def __init__(self):
        self.__BASE_URL = BASE_URL
        self._response = Response()

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    def _get(self, url: str, params=None, **kwargs) -> "BaseApi":
        response = requests.get(self.__BASE_URL + url, params, **kwargs)
        self._response = response

        return self

    def _post(self, url: str, body: PydanticModel, **kwargs) -> "BaseApi":
        response = requests.post(self.__BASE_URL + url, json=body.model_dump(exclude_none=True), **kwargs)
        self._response = response

        return self

    def _put(self, url: str, body: PydanticModel, headers: Mapping[str, str | bytes | None], **kwargs) -> "BaseApi":
        response = requests.put(self.__BASE_URL + url, json=body.model_dump(exclude_none=True), headers=headers,
                                **kwargs)
        self._response = response

        return self

    def _delete(self, url: str, headers: Mapping[str, str | bytes | None], **kwargs) -> "BaseApi":
        response = requests.delete(self.__BASE_URL + url, headers=headers, **kwargs)
        self._response = response

        return self

    def _patch(self, url: str, body: PydanticModel, headers: Mapping[str, str | bytes | None], **kwargs) -> "BaseApi":
        response = requests.patch(self.__BASE_URL + url, json=body.model_dump(exclude_none=True), headers=headers,
                                  **kwargs)
        self._response = response

        return self

    def _get_response_model(self, response_model: PydanticModel) -> PydanticModel:
        try:
            response_data = self._response.json()
        except JSONDecodeError:
            response_data = self._response.text

        try:
            return response_model.model_validate(response_data)
        except ValidationError:
            raise AssertionError(f'Response does not match Pydantic response model - {response_model}')

    def _check_response_status_code(self, expected_status_code: int) -> "BaseApi":
        assert self._response.status_code == expected_status_code, 'Unexpected status code! ' \
                                                                   f'Expected status code - {expected_status_code}, actual status code - {self._response.status_code}'

        return self
