from .interfaces import CarInterface, GarageInterface

def validate_interfaces(value: CarInterface | GarageInterface) -> None:
    
    if not isinstance(value, (CarInterface, GarageInterface)):
        raise TypeError