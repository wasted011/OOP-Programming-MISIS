from abc import ABC, abstractmethod
from datetime import date

class CarInterface(ABC):

    @property
    @abstractmethod
    def brand(self) -> str: pass

    @property
    @abstractmethod
    def model(self) -> str: pass

    @property
    @abstractmethod
    def mileage(self) -> int: pass

    @property
    @abstractmethod
    def year_of_manufacture(self) -> date: pass

    @abstractmethod
    def get_service_status(self) -> bool: pass

    @abstractmethod
    def drive(self, distance: int) -> int | tuple[int, int]: pass
    
class GarageInterface(ABC):

    @property
    @abstractmethod
    def garage(self) -> list[CarInterface]: pass
    
    @property
    @abstractmethod
    def max_cars(self) -> int: pass

    @abstractmethod
    def add(self, car: CarInterface) -> bool: pass
    
    @abstractmethod
    def remove(self, car: CarInterface) -> bool: pass
    
    @abstractmethod
    def remove_at(self, index: int) -> bool: pass
    
    @abstractmethod
    def get_all(self) -> list[CarInterface]: pass

class Printable(ABC):

    @abstractmethod
    def get_info(self) -> str: pass