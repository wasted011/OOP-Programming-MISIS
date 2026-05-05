from typing import TypeVar, Callable
from datetime import date
from src.lab_01.main.validate import validate_mileage

C = TypeVar('C')

# Функция для map():

def add_mileage(obj: C) -> int:
    return obj._mileage + 10000

# Фабрика функций:

def filter_by_mileage_fabric(mileage: int) -> Callable[[C], bool]:
    validate_mileage(mileage)
    def filter_by_mileage_func(obj: C) -> bool:
        return obj._mileage <= mileage
    return filter_by_mileage_func

# Ф-ии для сорт. методов коллекции:

def sort_by_brand(obj: C) -> str:
    return obj._brand

def sort_by_model(obj: C) -> str:
    return obj._model

def sort_by_mileage(obj: C) -> int:
    return obj._mileage

def sort_by_year_of_manufacture(obj: C) -> int:
    return obj._year_of_manufacture

# Ф-ии для для фильтр. методов коллекции:

def filter_by_brand(obj: C) -> bool:
    return obj._brand == "Toyota"

def filter_by_model(obj: C) -> bool:
    return obj._model == "Camry"

def filter_by_mileage(obj: C) -> bool:
    return obj._mileage <= 50000

def filter_by_year_of_manufacture(obj: C) -> bool:
    return obj._year_of_manufacture >= date(2020, 1, 1)

# Функции для apply() метода коллекции:

def apply_mileage_increase(obj: C) -> None:
    obj._mileage += 10000

def apply_mileage_decrease(obj: C) -> None:
    obj._mileage -= 10000


# Стратегии:

class IncreaseMileageStrategy:
    def __call__(self, obj: C) -> None:
        obj._mileage *= 1.5
        
class DecreaseMileageStrategy:
    def __call__(self, obj: C) -> None:
        obj._mileage *= 0.5
