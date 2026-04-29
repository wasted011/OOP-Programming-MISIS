def validate_type_int(value: int):

    if not isinstance(value, int):
        raise TypeError
    
def validate_charge_level(value: int):

    validate_type_int(value)
    
    if not (0 <= value <= 100):
        raise ValueError

def validate_max_speed(value: int):

    validate_type_int(value)
    
    if not (0 <= value <= 1000):
        raise ValueError
    
def validate_acceleration(value: int):

    validate_type_int(value)
    
    if not (0 <= value <= 7):
        raise ValueError

def validate_distance(value: int):
    validate_type_int(value)

    if value <= 0:
        raise ValueError

def validate_time(value: int):
    validate_type_int(value)
    
    if value <= 0:
        raise ValueError

def validate_battery_capacity(value: int):
    validate_type_int(value)
    
    if not (0 <= value <= 1000):
        raise ValueError