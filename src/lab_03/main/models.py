from dataclasses import dataclass
from .base import Car
from .validation import *

@dataclass
class ElectricCar(Car):

    _battery_capacity: int = 100
    _charge_level: int = 100

    def __repr__(self):

        return f"ElectricCar(battery_capacity={self._battery_capacity}, charge_level={self._charge_level})"

    def __post_init__(self):
        super().__post_init__()
        validate_charge_level(self._charge_level)

    @property
    def battery_capacity(self): return self._battery_capacity
    
    @property
    def charge_level(self): return self._charge_level
    
    @charge_level.setter
    def charge_level(self, value: int):

        validate_charge_level(value)
        self._charge_level = value

    @battery_capacity.setter
    def battery_capacity(self, value: int):

        validate_battery_capacity(value)
        self._battery_capacity = value

    def recharge(self, time: int):

        percentage = time // 10
        self._charge_level = min(100, self._charge_level + percentage)
        self._battery_capacity -= 1

        return f"Charge level: {self._charge_level}, Battery capacity: {self._battery_capacity}"
    def drive(self, distance):

        if self._charge_level <= 0:
            raise ValueError

        return super().drive(distance)

    def get_service_status(self):
        
        if self._charge_level <= 20:
            return "Charge level is low, please recharge"
        return super().get_service_status()
    
@dataclass
class SportCar(Car):

    _max_speed: int
    _acceleration: int

    def __repr__(self):

        return f"SportCar(max_speed={self._max_speed}, acceleration={self._acceleration})"
    
    def __post_init__(self):
        super().__post_init__()

        validate_max_speed(self._max_speed)
        validate_acceleration(self._acceleration)

    @property
    def max_speed(self): return self._max_speed

    @property
    def acceleration(self): return self._acceleration

    @max_speed.setter
    def max_speed(self, value: int):

        validate_max_speed(value)
        self._max_speed = value

    @acceleration.setter
    def acceleration(self, value: int):

        validate_acceleration(value)
        self._acceleration = value

    def distance_time(self, distance: int):
        
        validate_distance(distance)
        time = distance / self._acceleration

        return f"{distance}: {time}"

    def drive(self, distance):
        
        if self._mileage + distance > 100000:
            raise ValueError
        
        return super().drive(distance)

    def get_service_status(self):

        if self._mileage >= 100000:
            return "Service needed"

        return super().get_service_status()