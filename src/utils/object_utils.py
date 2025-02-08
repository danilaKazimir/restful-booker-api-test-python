from typing import TypeVar, Any, Dict

from pydantic import BaseModel
from deepdiff import DeepDiff

from src.models.booking.booking import Booking


class ObjectUtils:
    PydanticModel = TypeVar('PydanticModel', bound=BaseModel)

    @staticmethod
    def check_that_objects_content_are_identical(obj1: PydanticModel, obj2: PydanticModel) -> None:
        diff = DeepDiff(obj1, obj2)

        assert not diff, f'Objects are not identical! Differences - {diff}'

    @staticmethod
    def deep_update_model(target: PydanticModel, source: PydanticModel) -> PydanticModel:
        """
        Рекурсивно обновляет `target`, заменяя только те поля, которые есть в `source`
        и не являются `None`. Вложенные объекты также обновляются по тем же правилам.
        """

        def recursive_update(target_data: Dict[str, Any], source_data: Dict[str, Any]) -> Dict[str, Any]:
            updated_data = target_data.copy()
            for key, value in source_data.items():
                if value is None:
                    continue  # Пропускаем None, чтобы не затирать данные
                if isinstance(value, dict) and isinstance(target_data.get(key), dict):
                    # Рекурсивно обновляем вложенные словари
                    updated_data[key] = recursive_update(target_data[key], value)
                elif isinstance(value, BaseModel) and isinstance(target_data.get(key), BaseModel):
                    # Рекурсивно обновляем вложенные модели
                    updated_data[key] = Booking.deep_update_model(target_data[key],
                                                                  value)  # Рекурсивный вызов для модели
                else:
                    updated_data[key] = value  # Простые значения обновляем
            return updated_data

        # Получаем данные моделей как словари
        target_data = target.model_dump()
        source_data = source.model_dump()

        # Обновляем данные с помощью рекурсивного метода
        updated_data = recursive_update(target_data, source_data)

        # Возвращаем новый объект модели с обновлёнными данными
        return target.__class__(**updated_data)
