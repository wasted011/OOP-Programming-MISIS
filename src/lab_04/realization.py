from dataclasses import dataclass, field
from datetime import date

from .interfaces import CarInterface, GarageInterface, Printable

from .validations.validation_lab_01 import (
    validate_car_brand,
    validate_car_model,
    validate_mileage,
    validate_year_of_manufacture,
    validate_distance
)

from .validations.validation_lab_04 import (
    validate_interfaces
)

from .validations.validation_lab_02 import (
    validate_max_cars,
    validate_index
)

from .validations.validation_lab_03 import (
    validate_battery_capacity,
    validate_charge_level,
    validate_time
)

# Реализация интерфейса сущности Car (Основная информация, уведомление о посещении сервиса если self._mileage >= 1_000_000):

@dataclass
class Car(CarInterface, Printable):

    _brand: str
    _model: str
    _mileage: int
    _year_of_manufacture: date
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @property
    def model(self) -> str:
        return self._model
    
    @property
    def mileage(self) -> int:
        return self._mileage
    
    @property
    def year_of_manufacture(self) -> date:
        return self._year_of_manufacture

    @brand.setter
    def brand(self, value: str) -> None:

        validate_car_brand(value)
        self._brand = value
    
    @model.setter
    def model(self, value: str) -> None:

        validate_car_model(value)
        self._model = value
    
    @mileage.setter
    def mileage(self, value: int) -> None:

        validate_mileage(value)
        self._mileage = value
    
    @year_of_manufacture.setter
    def year_of_manufacture(self, value: date) -> None:

        validate_year_of_manufacture(value)
        self._year_of_manufacture = value
    
    def get_service_status(self) -> bool:

        if self._mileage >= 1_000_000:
            return True

        return False
    
    def drive(self, distance: int):

        validate_distance(distance)
        self._mileage += distance
        return self._mileage

    def get_info(self):
        return f"Car(brand={self._brand}, model={self._model}, mileage={self._mileage}, year_of_manufacture={self._year_of_manufacture})"

# Универсальная ф-ия, работающая через интерфейс:

def proccess_car(obj: Printable) -> str:
    
    if not isinstance(obj, Printable):
        raise TypeError("Object must implement Printable interface")
    
    return obj.get_info()

# Реализация коллекции Garage через интерфейс GarageInterface:

@dataclass
class Garage(GarageInterface, Printable):
    
    _garage: list[CarInterface] = field(default_factory=list)
    _max_cars: int = 10

    @property
    def garage(self) -> list[CarInterface]:
        return self._garage.copy()
    
    @property
    def max_cars(self) -> int:
        return self._max_cars
    
    @max_cars.setter
    def max_cars(self, value: int) -> None:

        validate_max_cars(value)
        self._max_cars = value

    def __len__(self) -> int:
        return len(self._garage)

    def __iter__(self) -> type[iter]:
        return iter(self._garage)

    def __getitem__(self, index: int) -> CarInterface:

        validate_index(index)
        return self._garage[index]

    def add(self, car: CarInterface) -> bool:
        
        validate_interfaces(car)
        
        if car not in self._garage:

            if len(self._garage) < self._max_cars:

                self._garage.append(car)
                return True

        return False

    def remove(self, car: CarInterface) -> bool:

        validate_interfaces(car)

        if self._garage:

            if car in self._garage:

                self._garage.remove(car)
                return True

        return False

    def remove_at(self, index: int) -> bool:
        
        validate_index(index)
        
        if self._garage:

            if index < len(self._garage):

                self._garage.pop(index)
                return True

        return False

    def get_all(self) -> list[CarInterface]:

        return self._garage.copy()

    def filter_by_interface(self, interface_type: type) -> list[CarInterface | GarageInterface]:
         
         validate_interfaces(interface_type)
         return [object for object in self._garage if isinstance(object, interface_type)]

    def get_info(self):
        return f"Garage(cars={len(self._garage)}, max_cars={self._max_cars})"

# Реализация дочернего класса Car через интерфейс CarInterface:

@dataclass
class ElectricCar(Car):

    _battery_capactiy: int = 100
    _charge_level: int = 100

    @property
    def battery_capacity(self) -> int:
        return self._battery_capactiy
    
    @property
    def charge_level(self) -> int:
        return self._charge_level
    
    @battery_capacity.setter
    def battery_capacity(self, value: int) -> None:
        
        validate_battery_capacity(value)
        self._battery_capactiy = value

    @charge_level.setter
    def charge_level(self, value: int) -> None:
        
        validate_charge_level(value)
        self._charge_level = value

    def charge(self, time: int) -> int:

        validate_time(time)

        amount_of_charge = time / 60
        self._charge_level += min(100, amount_of_charge)

        return self._charge_level

    def drive(self, distance: int) -> (int, int):

        validate_distance(distance)

        self._charge_level -= max(0, distance / 100)
        self._mileage += distance

        return self._charge_level, self._mileage