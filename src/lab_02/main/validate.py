from src.lab_01.main.model import Car

def validate_class_car(value: Car):

    if not isinstance(value, Car):
        raise TypeError

def validate_index(value: int):

    if not isinstance(value, int):
        raise TypeError
    
def validate_reverse(value: bool):
    
    if not isinstance(value, bool):
        raise TypeError
