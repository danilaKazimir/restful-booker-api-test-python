from typing import TypeVar, Any

from pydantic import BaseModel


class ObjectUtils:
    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    @staticmethod
    def get_attr(obj: PydanticModel, attr_path: str) -> Any:
        """
        Gets the value of an attribute by path. If attribute is nested, path is separated by dots.

        :param obj: The original object.
        :param attr_path: A string with the attribute path, examples - "totalprice" or "booking.bookingdates.checkin".
        :return: The attribute value.
        """
        if attr_path == 'root':
            return obj.root

        for attr in attr_path.split('.'):
            if not hasattr(obj, attr):
                raise AttributeError(f'Attribute path "{attr_path}" is invalid at "{attr}"')
            obj = getattr(obj, attr)

        attr_value = obj
        return attr_value

    @staticmethod
    def set_attr(obj: PydanticModel, attr_path: str, value: Any) -> None:
        """
        Sets the value of a nested attribute by following the provided path.
        The path is separated by dots, and the function navigates through the object until the last attribute
        to set its value.

        :param obj: The object where the attribute will be set.
        :param attr_path: A string representing the attribute path, e.g., "booking.bookingdates.checkin".
        :param value: The value to be set at the deepest level of the attribute path.
        """
        attrs = attr_path.split('.')
        for attr in attrs[:-1]:
            obj = getattr(obj, attr)
        setattr(obj, attrs[-1], value)
