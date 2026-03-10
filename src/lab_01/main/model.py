from dataclasses import dataclass
from datetime import date

from src.lab_01.main.validate import (

    validate_car_brand,
    validate_car_model,
    validate_mileage,
    validate_year_of_manufacture,
    validate_car_funcs_drive_mode,
    validate_car_funcs_car,
    validate_distance
    
)

# --// Создание класса Car с атрибутами: марка, модель, пробег, год выпуска. \\--

@dataclass
class Car:

    # --// Инициализация атрибутов дата-класса Car \\--

    _brand: str
    _model: str
    _mileage: int
    _year_of_manufacture: date

    # --\\ ------------------------------------------------- //--

    # --//  Валидация атрибутов дата-класса Car при его создании и при изменении атрибутов через сеттеры.  \\--

    def __post_init__(self):

        if not validate_car_brand(self._brand):
            raise ValueError("Invalid brand value.")
        
        if not validate_car_model(self._model):
            raise ValueError("Invalid model value.")
        
        if not validate_mileage(self._mileage):
            raise ValueError("Invalid mileage value.")
        
        if not validate_year_of_manufacture(self._year_of_manufacture):
            raise ValueError("Invalid year of manufacture value.")
    
    @property
    def brand(self): return self._brand
    
    @property
    def model(self): return self._model
    
    @property
    def mileage(self): return self._mileage
    
    @property
    def year_of_manufacture(self): return self._year_of_manufacture

    @brand.setter
    def brand(self, value: str):

        if not validate_car_brand(value):
            raise ValueError("Invalid brand value.")
        
        self._brand = value
    
    @model.setter
    def model(self, value: str):

        if not validate_car_model(value):
            raise ValueError("Invalid model value.")
        
        self._model = value
    
    @mileage.setter
    def mileage(self, value: int):

        if not validate_mileage(value):
            raise ValueError("Invalid mileage value.")
        
        self._mileage = value
    
    @year_of_manufacture.setter
    def year_of_manufacture(self, value: date):

        if not validate_year_of_manufacture(value):
            raise ValueError("Invalid year of manufacture value.")
        
        self._year_of_manufacture = value

    # --\\ ------------------------------------------------- //--

    # --// Реализация методов __str__, __repr__, __eq__ для дата-класса Car. (Реализация Thunder-методов, в dataclass их можно не прописывать)  \\--

    def __str__(self):
        return f"Car: {self._brand} {self._model}, Mileage: {self.mileage}, Year of Manufacture: {self._year_of_manufacture}"
    
    def __repr__(self):
        return f"Car(brand='{self._brand}', model='{self._model}', mileage={self.mileage}, year_of_manufacture={self._year_of_manufacture})"
    
    def __eq__(self, value):

        if not isinstance(value, Car):
            return NotImplemented
        
        return (self._brand == value._brand and
                self._model == value._model and
                self.mileage == value.mileage and
                self._year_of_manufacture == value._year_of_manufacture)
    
    # --\\ ------------------------------------------------- //--

# --// Создание класса CarFuncs, который будет содержать атрибуты, связанные с функциями автомобиля (например, состояние двигателя, света, сигналов и т.д.) и методы для управления этими функциями. \\--
    
@dataclass
class CarFuncs:

    # --// Инициализация атрибутов дата-класса CarFuncs \\--

    _car: Car
    engine: bool
    lights: bool
    signals: bool
    drive_mod: str
    
    # --\\ ------------------------------------------------- //--

    # --// Валидация атрибутов дата-класса CarFuncs при его создании и при изменении атрибутов через сеттеры.  \\--

    @property
    def car(self): return self._car 
    
    @car.setter
    def car(self, value: Car):

        if not validate_car_funcs_car(value):
            raise ValueError("Invalid car value.")
        
        self._car = value
    
    # --\\ ------------------------------------------------- //--

    # --// Пост-валидация атрибутов дата-класса CarFuncs при его создании.  \\--

    def __post_init__(self):
        
        if not all(isinstance(value, bool) for value in [self.lights, self.signals, self.engine]):
            raise ValueError("Invalid lights, signals or engine value.")
        
        if not validate_car_funcs_drive_mode(self.drive_mod):
            raise ValueError("Invalid drive mode value.")
    
    # --\\ ------------------------------------------------- //--

    # --// Реализация методов __str__, __repr__, __eq__ для дата-класса CarFuncs. (Реализация Thunder-методов, в dataclass их можно не прописывать)  \\--

    def __str__(self):
        return f"Car Functions: Engine: {'On' if self.engine else 'Off'}, Lights: {'On' if self.lights else 'Off'}, Signals: {'On' if self.signals else 'Off'}, Drive Mode: {self.drive_mod}"
    
    def __repr__(self):
        return f"CarFuncs(engine={self.engine}, lights={self.lights}, signals={self.signals}, drive_mod='{self.drive_mod}')"
    
    def __eq__(self, value):

        if not isinstance(value, CarFuncs):
            return NotImplemented
        
        return (self.car == value.car and
                self.engine == value.engine and
                self.lights == value.lights and
                self.signals == value.signals and
                self.drive_mod == value.drive_mod)
    
    # --\\ ------------------------------------------------- //--

    # --// Реализация методов для управления функциями автомобиля (например, включение/выключение двигателя, света, сигналов и т.д.)  \\--

    def toggle_main_car_func_engine(self):
        
        self.engine = not(self.engine)
        return f"Engine turned {'On' if self.engine else 'Off'}."
    
    def toggle_car_funcs(self, value: str):
        
        
        if value in ['lights', 'signals']:

            if self.engine:

                if value == 'lights':

                    self.lights = not(self.lights)
                    return f"Lights turned {'On' if self.lights else 'Off'}."
                
                elif value == 'signals':

                    self.signals = not(self.signals)
                    return f"Signals turned {'On' if self.signals else 'Off'}."
                
            return ValueError(f"Cannot toggle {value}. The engine is off.")

        return f'Invalid function: {value}. Valid options are: lights, signals.'
    
    def toggle_drive_mod(self, value: str):

        if value in ['Forward', 'Reverse', 'Neutral']:

            if self.engine:
                
                if value != self.drive_mod:
                    self.drive_mod = value
                    return f"Drive mode set to: {self.drive_mod}"
                
                return f"Drive_mod is already set on {value}"
            
            return "Cannot change drive mode. The engine is off."
        
        return f'Invalid drive mode: {value}. Valid options are: Forward, Reverse, Neutral.'
    
    # --\\-----------------------------------------------------------------------------------------//--
    
    # --// Реализация метода drive, который принимает количество километров, на которое нужно проехать, и увеличивает пробег автомобиля на это количество.  \\--
    
    def drive(self, distance: int):

        if not validate_distance(distance):
            raise ValueError("Invalid distance value.")
        
        if self.engine:

            self._car.mileage += distance
            return f"Car driven for {distance} km. Total mileage is now {self._car.mileage} km."
        
        return "Cannot drive. The engine is off."
    
    # --\\ -------------------------------------------------------------------------------- //--
