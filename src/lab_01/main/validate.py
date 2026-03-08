from datetime import date       

def validate_car_brand(variable: str) -> bool:

    return isinstance(variable, str) and variable != ''
        
def validate_car_model(variable: str) -> bool:

    return isinstance(variable, str) and variable != ''

def validate_mileage(variable: int) -> bool:

    return isinstance(variable, int) and variable >= 0

def validate_year_of_manufacture(variable: date) -> bool:

    return isinstance(variable, date) and variable <= date.today()

def validate_car_funcs_drive_mode(drive_mod: str) -> bool:

    return isinstance(drive_mod, str) and drive_mod != ''

def validate_car_funcs_car(object) -> bool:
    
    from src.lab_01.main.model import Car

    return isinstance(object, Car)

def validate_distance(distance: int) -> bool:

    return isinstance(distance, int) and distance >= 0

