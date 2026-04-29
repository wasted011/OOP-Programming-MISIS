from datetime import date

def validate_car_brand(variable: str) -> bool:

    return isinstance(variable, str) and len(variable.split()) != 0


def validate_car_model(variable: str) -> bool:

    return isinstance(variable, str) and len(variable.split()) != 0

def validate_mileage(variable: int) -> bool:

    return isinstance(variable, int) and variable >= 0

def validate_year_of_manufacture(variable: date) -> bool:

    return isinstance(variable, date) and variable <= date.today()

def validate_lights_signals(variable_01: bool, variable_02: bool):
    
    return all(isinstance(element, bool) for element in [variable_01, variable_02])
        
def validate_car_funcs_drive_mode(drive_mod: str) -> bool:

    return isinstance(drive_mod, str) and len(drive_mod.split()) != 0

def validate_distance(distance: int) -> bool:

    return isinstance(distance, int) and distance >= 0