from dataclasses import dataclass
from datetime import date

@dataclass
class Car:
    """
    Базовый класс, представляющий автомобиль.
    Содержит основные характеристики: ID, марка, модель, пробег и год выпуска.
    """
    id: int
    brand: str
    model: str
    mileage: int
    year_of_manufacture: date

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"[{self.id}] {self.brand} {self.model} ({self.year_of_manufacture.year}), Пробег: {self.mileage}км"

    def to_dict(self) -> dict:
        """
        Преобразует объект в словарь для последующего сохранения в JSON.
        
        :return: Словарь с данными объекта и указанием типа.
        """
        return {
            "type": "Car",
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "mileage": self.mileage,
            "year_of_manufacture": self.year_of_manufacture.isoformat()
        }

@dataclass
class ElectricCar(Car):
    """
    Класс, представляющий электромобиль.
    Расширяет базовый автомобиль параметрами батареи и уровня заряда.
    """
    battery_capacity: int
    charge_level: int

    def __str__(self) -> str:
        """Возвращает строковое представление электромобиля."""
        base_str = super().__str__()
        return f"{base_str} [Электро: {self.charge_level}/{self.battery_capacity}кВт·ч]"

    def to_dict(self) -> dict:
        """
        Преобразует объект электромобиля в словарь.
        
        :return: Расширенный словарь с данными электромобиля.
        """
        data = super().to_dict()
        data.update({
            "type": "ElectricCar",
            "battery_capacity": self.battery_capacity,
            "charge_level": self.charge_level
        })
        return data

@dataclass
class SportCar(Car):
    """
    Класс, представляющий спортивный автомобиль.
    Расширяет базовый автомобиль параметрами скорости и динамики.
    """
    max_speed: int
    acceleration: float

    def __str__(self) -> str:
        """Возвращает строковое представление спортивного автомобиля."""
        base_str = super().__str__()
        return f"{base_str} [Спорт: Макс. скорость {self.max_speed}км/ч, 0-100 за {self.acceleration}с]"

    def to_dict(self) -> dict:
        """
        Преобразует объект спортивного автомобиля в словарь.
        
        :return: Расширенный словарь с данными спорткара.
        """
        data = super().to_dict()
        data.update({
            "type": "SportCar",
            "max_speed": self.max_speed,
            "acceleration": self.acceleration
        })
        return data
