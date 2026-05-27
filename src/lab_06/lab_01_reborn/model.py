from dataclasses import dataclass
from datetime import date
from multiprocessing import Value

from .validate import (
    validate_car_brand,
    validate_car_model,
    validate_mileage,
    validate_year_of_manufacture,
    validate_lights_signals,
    validate_car_funcs_drive_mode,
    validate_distance,
)

# Инициализация дата-класса Car с атрибутами: марка, модель, пробег, год выпуска.

@dataclass
class Car:

    # Инициализация атрибутов дата-класса Car.

    _brand: str 
    _model: str 
    _mileage: int 
    _year_of_manufacture: date 

    # Валидация атрибутов дата-класса Car при его создании и при изменении атрибутов через сеттеры. 

    def __post_init__(self) -> None:

        if not validate_car_brand(self._brand):
            raise ValueError("Invalid brand value.")

        if not validate_car_model(self._model):
            raise ValueError("Invalid model value.")

        if not validate_mileage(self._mileage):
            raise ValueError("Invalid mileage value.")

        if not validate_year_of_manufacture(self._year_of_manufacture):
            raise ValueError("Invalid year of manufacture value.")

    # Инициализация геттеров для защищенных атрибутов дата-класса Car.
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

    # Инициализация сеттеров для защищенных атрибутов дата-класса Car (Сеттеры не могут существовать без геттеров).

    @brand.setter
    def brand(self, value: str) -> None:

        if not validate_car_brand(value):
            raise ValueError("Invalid brand value.")

        self._brand = value

    @model.setter
    def model(self, value: str) -> None:

        if not validate_car_model(value):
            raise ValueError("Invalid model value.")

        self._model = value

    @mileage.setter
    def mileage(self, value: int) -> None:

        if not validate_mileage(value):
            raise ValueError("Invalid mileage value.")

        self._mileage = value

    @year_of_manufacture.setter
    def year_of_manufacture(self, value: date) -> None:

        if not validate_year_of_manufacture(value):
            raise ValueError("Invalid year of manufacture value.")

        self._year_of_manufacture = value

    # Реализация методов __str__, __repr__, __eq__ для дата-класса Car. (Dunder-методы в dataclass их можно не прописывать).

    def __str__(self) -> str:
        return f"Car: {self._brand} {self._model}, Mileage: {self.mileage}, Year of Manufacture: {self._year_of_manufacture}"

    def __repr__(self) -> str:
        return f"Car(brand='{self._brand}', model='{self._model}', mileage={self.mileage}, year_of_manufacture={self._year_of_manufacture})"

    def __eq__(self, value: Car) -> bool:

        if not isinstance(value, Car):
            return NotImplemented

        return (
            self._brand == value._brand
            and self._model == value._model
            and self.mileage == value.mileage
            and self._year_of_manufacture == value._year_of_manufacture
        )

    def get_service_status(self) -> str:

        if self._mileage >= 500000:
            return "Service needed"

        return "Service not needed" 
        
# Инициализация класса CarFuncs, который содержит атрибуты, связанные с функциями автомобиля и методы для управления этими функциями.

@dataclass
class CarFuncs:

    # Инициализация атрибутов дата-класса CarFuncs.

    _car: Car
    engine: bool
    lights: bool
    signals: bool
    drive_mod: str

    # Инициализация геттера класса CarFuncs.

    @property
    def car(self) -> Car:
        return self._car

    # Инициализация сеттера класса CarFuncs.

    @car.setter
    def car(self, value: Car) -> None:

        if not isinstance(value, Car):
            raise ValueError("Invalid car value.")
        
        self._car = value

    # Валидация атрибутов дата-класса CarFuncs при его создании.

    def __post_init__(self) -> None:

        
        if not validate_lights_signals(self.lights, self.signals):
            raise ValueError("Invalid lights, signals or engine value.")

        if not validate_car_funcs_drive_mode(self.drive_mod):
            raise ValueError("Invalid drive mode value.")

    # Реализация методов __str__, __repr__, __eq__ для дата-класса CarFuncs. (Dunder-методы в dataclass их можно не прописывать).

    def __str__(self) -> str:
        return f"Car Functions: Engine: {'On' if self.engine else 'Off'}, Lights: {'On' if self.lights else 'Off'}, Signals: {'On' if self.signals else 'Off'}, Drive Mode: {self.drive_mod}"

    def __repr__(self) -> str:
        return f"CarFuncs(engine={self.engine}, lights={self.lights}, signals={self.signals}, drive_mod='{self.drive_mod}')"

    def __eq__(self, value: CarFuncs) -> bool:

        if not isinstance(value, CarFuncs):
            return NotImplemented

        return (
            self.car == value.car
            and self.engine == value.engine
            and self.lights == value.lights
            and self.signals == value.signals
            and self.drive_mod == value.drive_mod
        )

    # Реализация метода включение двигателя автомобиля (Выведен отдельно потому что self.engine - атрибут состояние, от него зависят последующие методы).

    def toggle_main_car_func_engine(self) -> str:

        self.engine = not (self.engine)
        return f"Engine turned {'On' if self.engine else 'Off'}."

    # Реализация метода включения/выключения фонарей/сигналов.

    def toggle_car_funcs(self, value: str) -> str:

        if value in ["lights", "signals"]:

            if self.engine:

                if value == "lights":

                    self.lights = not (self.lights)
                    return f"Lights turned {'On' if self.lights else 'Off'}."

                elif value == "signals":

                    self.signals = not (self.signals)
                    return f"Signals turned {'On' if self.signals else 'Off'}."

            raise ValueError(f"Cannot toggle {value}. The engine is off.")

        return f"Invalid function: {value}. Valid options are: lights, signals."

    # Реализация метода переключения коробки передач.

    def toggle_drive_mod(self, value: str) -> str:

        if value in ["Forward", "Reverse", "Neutral"]:

            if self.engine:

                if value != self.drive_mod:
                    self.drive_mod = value
                    return f"Drive mode set to: {self.drive_mod}"

                return f"Drive_mod is already set on {value}"

            return "Cannot change drive mode. The engine is off."

        return f"Invalid drive mode: {value}. Valid options are: Forward, Reverse, Neutral."

    # Реализация метода drive, который принимает количество километров, на которое нужно проехать, и увеличивает пробег автомобиля.

    def drive(self, distance: int) -> str:

        if not validate_distance(distance):
            raise ValueError("Invalid distance value.")

        if self.engine:

            self._car.mileage += distance
            return f"Car driven for {distance} km. Total mileage is now {self._car.mileage} km."

        return "Cannot drive. The engine is off."