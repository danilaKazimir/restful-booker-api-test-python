from typing import TypeVar

import requests
from pydantic import BaseModel
from requests import Response

from config import BASE_URL


class BaseRequest:
    def __init__(self, base_url: str = BASE_URL):
        self.__BASE_URL = base_url
        self._response = Response()

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    def _get(self, url: str, params=None, **kwargs) -> "BaseRequest":
        response = requests.get(BASE_URL + url, params, **kwargs)
        self._response = response

        return self

    def _post(self, url: str, body: PydanticModel, **kwargs) -> "BaseRequest":
        response = requests.post(BASE_URL + url, json=body.model_dump(), **kwargs)
        self._response = response

        return self
