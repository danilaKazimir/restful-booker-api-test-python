from typing import TypeVar

from pydantic import BaseModel
from requests import JSONDecodeError

from src.base.base_request import BaseRequest


class BaseResponse(BaseRequest):
    def __init__(self):
        super().__init__()

    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    def _assert_response_status_code(self, expected_status_code: int):
        print(self._response.status_code)
        assert self._response.status_code == expected_status_code

        return self

    def _get_response_model(self, response_model: PydanticModel) -> PydanticModel:
        try:
            return response_model.model_validate(self._response.json())
        except JSONDecodeError:
            return response_model.model_validate(self._response.text)
