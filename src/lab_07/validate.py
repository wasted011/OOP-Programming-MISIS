from datetime import date
from typing import Any

def validate_id(car_id: Any) -> None:
    """
    Валидация уникального идентификатора автомобиля.
    
    :param car_id: Значение ID для проверки.
    :raises ValueError: Если ID не является целым неотрицательным числом.
    """
    try:
        val = int(car_id)
        if val < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("ID должен быть неотрицательным целым числом.")

def validate_string(value: Any, name: str) -> None:
    """
    Валидация текстовых полей на пустоту.
    
    :param value: Проверяемое строковое значение.
    :param name: Название поля для вывода в ошибке.
    :raises ValueError: Если строка пуста или некорректна.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} должен быть непустой строкой.")

def validate_mileage(mileage: Any) -> None:
    """
    Валидация значения пробега автомобиля.
    
    :param mileage: Значение пробега для проверки.
    :raises ValueError: Если пробег отрицателен или не является числом.
    """
    try:
        val = int(mileage)
        if val < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("Пробег должен быть неотрицательным целым числом.")

def validate_year(year: Any) -> None:
    """
    Валидация года выпуска автомобиля (от 1886 года до текущего).
    
    :param year: Год выпуска для проверки.
    :raises ValueError: Если год выходит за допустимые границы.
    """
    try:
        val = int(year)
        if val < 1886 or val > date.today().year:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(f"Год выпуска должен быть между 1886 и {date.today().year}.")

def validate_positive_int(value: Any, name: str) -> None:
    """
    Валидация целого положительного числа.
    
    :param value: Значение для проверки.
    :param name: Название поля.
    :raises ValueError: Если число не является положительным целым.
    """
    try:
        val = int(value)
        if val <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(f"{name} должен быть положительным целым числом.")

def validate_positive_float(value: Any, name: str) -> None:
    """
    Валидация положительного числа с плавающей точкой.
    
    :param value: Значение для проверки.
    :param name: Название поля.
    :raises ValueError: Если число не является положительным.
    """
    try:
        val = float(value)
        if val <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(f"{name} должен быть положительным числом.")
