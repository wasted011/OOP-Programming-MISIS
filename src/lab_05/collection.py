from datetime import date
from src.lab_01.main.model import Car
from src.lab_01.main.validate import (
    validate_mileage
)
from src.lab_02.main.validate import (
    validate_class_car,
    validate_index,
    validate_max_cars
)
from src.lab_03.main.models import ElectricCar, SportCar
from dataclasses import dataclass, field
from .validation_lab_05 import validate_callable
import copy

from typing import Callable

@dataclass
class Garage:

    _garage: list = field(default_factory=list)
    _max_cars: int = 10

    @property
    def garage(self): return self._garage[:]

    @property
    def max_cars(self): return self._max_cars

    @max_cars.setter
    def max_cars(self, value: int) -> None:

        validate_max_cars(value)
        self._max_cars = value

    def __len__(self): return len(self._garage)

    def __iter__(self): return iter(self._garage)

    def __getitem__(self, index: int): 

        validate_index(index)
        return self._garage[index]

    def add(self, car: Car | ElectricCar | SportCar) -> bool:

        validate_class_car(car)
        
        if car not in self._garage:
            if len(self._garage) < self._max_cars:
                self._garage.append(car)
                return True
            
            raise IndexError
        return False
    
    def remove(self, car: Car | ElectricCar | SportCar):

        validate_class_car(car)

        if car in self._garage:
            self._garage.remove(car)
            return True
        
        return False
    
    def get_all(self):
        return self._garage[:]
    
    def find_by_mileage(self, mileage_input: int):
        
        validate_mileage(mileage_input)

        if self._garage:
            for element in self._garage:
                if element._mileage == mileage_input:
                    return element
                
        return None
    def remove_at(self, index: int):
        
        validate_index(index)
        
        if index < len(self._garage):
            
            self._garage.pop(index)
            return True
        
        return False
    
    def get_most_used(self):
        
        if not self._garage: return []
        average_mileage = sum(element._mileage for element in self._garage) / len(self._garage)
        return [car for car in self._garage if car._mileage >= average_mileage]
    
    def get_oldest(self):

        
        if not self._garage: return []
        average_year_of_manufacture = sum(element._year_of_manufacture.year for element in self._garage) / len(self._garage)
        return [car for car in self._garage if car._year_of_manufacture.year <= average_year_of_manufacture]

    def get_vehicle_by_type(self, vehicle_type: type):
        
        if not self._garage: return []
        return [car for car in self._garage if isinstance(car, vehicle_type)]

    # Сортировка (на вход принимает функцию-стратегию):

    def sort_by(self, key: Callable[[], str | int | date]):

        validate_callable(key)
        self._garage.sort(key=key)
        return self
    
    # Фильтрация по функции-стратегии:

    def filter_by(self, predicate):

        validate_callable(predicate)
        self._garage = [car for car in self._garage if predicate(car)]
        return self

    def apply(self, operation):
        
        validate_callable(operation)
        copy_collection = copy.deepcopy(self)
        
        for obj in copy_collection:
            operation(obj)
        return copy_collection
        