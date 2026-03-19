from model import Car, CarFuncs
from dataclasses import dataclass
from random import randint
from datetime import date

@dataclass
class Garage:

    _car: Car
    _carfuncs: CarFuncs
    _items: list = []

    @property
    def car(self): return self._car

    @car.setter
    def car_setter(self, value: Car):

        if not isinstance(value, Car):
            raise ValueError
        
        self._car = value

    @property
    def carfuncs(self): return self._carfuncs

    @carfuncs.setter
    def carfuncs_setter(self, value: CarFuncs):

        if not isinstance(value, CarFuncs):
            raise ValueError
        
        self._carfuncs = value

    def __post_init__(self):

        if not isinstance(self._carfuncs, list):
            raise ValueError
    
    def add_car(self, object: CarFuncs):

        if not isinstance(object, CarFuncs):
            raise ValueError
        
        new_car = {randint(1,1000):{"Brand": self.car.brand, "Model": self.car.model, "Mileage":
        self.car.mileage, "Year_of_manufacture": self.car.year_of_manufacture,
        "CarFuncs": {"Engine": self.carfuncs.engine, "Lights": self.carfuncs.lights,
        "Signals": self.carfuncs.signals, "Drive_mod": self.carfuncs.drive_mod}}}

        self._items.append(new_car)
        return self._items

car_object = Car("Toyota", "Camry", 0, date(2015, 1, 1)) 
object = CarFuncs(car_object, False, False, False, "Neutral")

print(Garage.add_car(object=object))