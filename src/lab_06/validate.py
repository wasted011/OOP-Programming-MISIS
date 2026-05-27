from typing import Any

def validate_max_items(value: int) -> None:

    if not isinstance(value, int):
        raise TypeError
    
    if value < 1:
        raise ValueError

def validate_generic_type(obj: Any, expected: type) -> None:

    if not isinstance(obj, expected):
        raise TypeError

def validate_mileage(value: int) -> None:

    if not isinstance(value, int):
        raise TypeError
    
    if value < 0:
        raise ValueError

def validate_index(value: int) -> None:
    
    if not isinstance(value, int):
        raise TypeError
    
    if value < 0:
        raise ValueError

def validate_callable(value: callable) -> None:
    
    if not callable(value):
        raise TypeError