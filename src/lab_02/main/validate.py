from src.lab_01.main.model import Car
from src.lab_03.main.models import ElectricCar, SportCar

def validate_class_car(value: Car | ElectricCar | SportCar):

    if not isinstance(value, (Car, ElectricCar, SportCar)):
        raise TypeError

def validate_index(value: int):

    if not isinstance(value, int):
        raise TypeError
    
def validate_reverse(value: bool):
    
    if not isinstance(value, bool):
        raise TypeError

def validate_max_cars(value: int):

    if not isistance(value, int):
        raise TypeError
    
    if value < 0:
        raise ValueError


