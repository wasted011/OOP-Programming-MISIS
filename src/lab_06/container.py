from datetime import date
from typing import TypeVar, Generic, Protocol, Callable, Any
from dataclasses import dataclass, field

from .validate import (
    validate_generic_type,
    validate_max_items,
    validate_mileage,
    validate_index,
    validate_callable
)

from src.lab_03.main.base import Car

T = TypeVar('T', bound=Car)
R = TypeVar('R')

class Mapable(Protocol):

    def map_by(self, function: Callable[[T], R]) -> list[R]:
        ...

class Sortable(Protocol):

    def sort_by(self, key: Callable[[T], str | int | date]) -> None:
        ...

class Displayable(Protocol):

    def get_service_status(self) -> str:
        ...

class Scorable(Protocol):

    def recharge(self, time: int) -> str:
        ...

M = TypeVar('M', bound=Mapable)
S = TypeVar('S', bound=Sortable)
D = TypeVar('D', bound=Displayable)
Sc = TypeVar('Sc', bound=Scorable)

@dataclass
class TypedCollection(Generic[T]):

    _items: list[T] = field(default_factory=list)
    _max_items: int = 10

    @property
    def items(self) -> list[T]:
        return self._items.copy()
    
    @property
    def max_items(self) -> int:
        return self._max_items
    
    @max_items.setter
    def max_items(self, value: int) -> None:
        validate_max_items(value)
        self._max_items = value
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        return f"TypedCollection({self._items})"
    
    def __repr__(self) -> str:
        return f"TypedCollection({self._items})"

    def add(self, item: T) -> None:

        validate_generic_type(item, T)

        if item not in self._items:
            if len(self._items) < self._max_items:
                self._items.append(item)

    
    def remove(self, item: T) -> None:

        validate_generic_type(item, T)
        if self._items:
            if item in self._items:
                self._items.remove(item)
    
    def get_all(self) -> list[T]:
        return self._items.copy()
    
    def find_by_mileage(self, mileage: int) -> T | None:

        validate_mileage(mileage)
        for item in self._items:
            if item._mileage == mileage:
                return item
    
    def remove_at(self, index: int) -> None:

        validate_index(index)
        if self._items:
            if index < len(self._items):
                self._items.pop(index)
        
    def get_most_used(self) -> list[T]:

        if not self._items: return []
        average_mileage = sum(item._mileage for item in self._items) / len(self._items)
        return [item for item in self._items if item._mileage >= average_mileage]
    
    def get_oldest(self) -> list[T]:

        if not self._items: return []
        average_year = sum(item._year_of_manufacture.year for item in self._items) / len(self._items)
        return [item for item in self._items if item._year_of_manufacture.year <= average_year]

    def get_vehicle_by_type(self, vehicle_type: type) -> list[T]:
        
        if not self._items: return []
        return [item for item in self._items if isinstance(item, vehicle_type)]

    def sort_by(self, key: Callable[[], str | int | date]) -> None:
        
        validate_callable(key)
        self._items.sort(key=key)

    def filter_by(self, predicate: Callable[[T], bool]) -> list[T]:
        
        validate_callable(predicate)
        return [item for item in self._items if predicate(item)]

    def apply(self, operation: Callable[[T], None]) -> None:
        
        validate_callable(operation)
        for item in self._items:
            operation(item)

    def find_by(self, predicate: Callable[[T], bool]) -> T | None:
        
        validate_callable(predicate)
        for item in self._items:
            if predicate(item):
                return item

    def map_by(self, function: Callable[[T], R]) -> list[R]:
        
        validate_callable(function)
        return [function(item) for item in self._items]
