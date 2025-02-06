from typing import TypeVar, Any, Mapping

import requests
from requests import Response
from pydantic import BaseModel, ValidationError
from requests import JSONDecodeError

from config import BASE_URL
from src.utils.object_utils import ObjectUtils


class BaseApi:
    def __init__(self):
        self.__BASE_URL = BASE_URL
        self._response = Response()
        self._response_model: BaseModel | None = None
        self._request: BaseModel | None = None

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    def _get(self, url: str, params=None, **kwargs) -> "BaseApi":
        response = requests.get(self.__BASE_URL + url, params, **kwargs)
        self._response = response

        return self

    def _post(self, url: str, body: PydanticModel, **kwargs) -> "BaseApi":
        response = requests.post(self.__BASE_URL + url, json=body.model_dump(), **kwargs)
        self._response = response

        return self

    def _put(self, url: str, body: PydanticModel, headers: Mapping[str, str | bytes | None], **kwargs) -> "BaseApi":
        response = requests.put(self.__BASE_URL + url, json=body.model_dump(), headers=headers, **kwargs)
        self._response = response

        return self

    def _get_response_model(self, response_model: PydanticModel) -> None:
        try:
            response_data = self._response.json()
        except JSONDecodeError:
            response_data = self._response.text

        try:
            self._response_model = response_model.model_validate(response_data)
        except ValidationError:
            raise AssertionError(f'Response does not match Pydantic response model - {response_model}')

    def _check_response_status_code(self, expected_status_code: int) -> None:
        assert self._response.status_code == expected_status_code, 'Unexpected status code! ' \
            f'Expected status code - {expected_status_code}, actual status code - {self._response.status_code}'

    def _check_response_field_value(self, field_path: str, expected_value: Any, extra_message: str = None) -> None:
        actual_value = ObjectUtils.get_attr(self._response_model, field_path)
        assert actual_value == expected_value, f'{extra_message} Expected {field_path} value = {expected_value}, ' \
            f'actual {field_path} value = {actual_value}'
