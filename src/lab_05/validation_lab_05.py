def validate_callable(value: callable) -> None:
    
    if not callable(value):
        raise TypeError