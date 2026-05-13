from typing import Any, TypeVar

def validate_max_items(value: int) -> None:

    if not isinstance(value, int):
        raise TypeError
    
    if value < 1:
        raise ValueError

def validate_generic_type(obj: Any, expected: Any) -> None:

    if isinstance(expected, TypeVar):
        if expected.__bound__ is None:
            return
        expected = expected.__bound__

    if not isinstance(obj, expected):
        raise TypeError(f"Expected {expected}, got {type(obj)}")

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

def validate_callable(value: Any) -> None:
    
    if not callable(value):
        raise TypeError
