from typing import Callable, Any
from datetime import date
from models import Car, ElectricCar, SportCar
from exceptions import CarNotFoundError, DuplicateCarError, InvalidDataError
from storage import save_collection, load_collection
from validate import (
    validate_id, validate_string, validate_mileage, 
    validate_year, validate_positive_int, validate_positive_float
)

class CarApp:
    """
    Класс приложения (Service Layer) для управления коллекцией автомобилей.
    """
    
    def __init__(self, storage_path: str = "Saved/cars.json"):
        """
        Инициализация приложения и загрузка данных.
        
        :param storage_path: Путь к JSON файлу для хранения данных.
        """
        self._storage_path: str = storage_path
        self._cars: list[Car] = load_collection(self._storage_path)
        self._types_map = {
            "standard": Car,
            "electric": ElectricCar,
            "sport": SportCar
        }

    def add_car(self, car_type: str, **kwargs) -> Car:
        """
        Создает и добавляет новый автомобиль в коллекцию.
        
        :param car_type: Тип автомобиля ('standard', 'electric', 'sport').
        :param kwargs: Параметры для конструктора автомобиля.
        :return: Созданный объект автомобиля.
        :raises DuplicateCarError: Если автомобиль с таким ID уже существует.
        :raises InvalidDataError: Если данные некорректны.
        """
        try:
            # Общая валидация
            validate_id(kwargs.get("id"))
            validate_string(kwargs.get("brand"), "Марка")
            validate_string(kwargs.get("model"), "Модель")
            validate_mileage(kwargs.get("mileage"))
            
            year_val = kwargs.get("year_of_manufacture")
            if isinstance(year_val, date):
                validate_year(year_val.year)
            else:
                validate_year(year_val)
                kwargs["year_of_manufacture"] = date(int(year_val), 1, 1)

            # Валидация специфичных полей
            if car_type == "electric":
                validate_positive_int(kwargs.get("battery_capacity"), "Емкость батареи")
                validate_positive_int(kwargs.get("charge_level"), "Уровень заряда")
            elif car_type == "sport":
                validate_positive_int(kwargs.get("max_speed"), "Максимальная скорость")
                validate_positive_float(kwargs.get("acceleration"), "Разгон")

            if any(c.id == kwargs["id"] for c in self._cars):
                raise DuplicateCarError(kwargs["id"])

            cls = self._types_map.get(car_type)
            if not cls:
                raise InvalidDataError(f"Неизвестный тип автомобиля: {car_type}")

            new_car = cls(**kwargs)
            self._cars.append(new_car)
            return new_car
            
        except ValueError as e:
            raise InvalidDataError(str(e))

    def delete_car(self, car_id: int) -> None:
        """
        Удаляет автомобиль из коллекции по его ID.
        
        :param car_id: Уникальный идентификатор автомобиля.
        :raises CarNotFoundError: Если автомобиль с данным ID не найден.
        """
        for i, car in enumerate(self._cars):
            if car.id == car_id:
                self._cars.pop(i)
                return
        raise CarNotFoundError(car_id)

    def find_car_by_id(self, car_id: int) -> Car:
        """
        Выполняет поиск автомобиля по его ID.
        
        :param car_id: Уникальный идентификатор искомого автомобиля.
        :return: Объект найденного автомобиля.
        :raises CarNotFoundError: Если автомобиль с таким ID не найден.
        """
        for car in self._cars:
            if car.id == car_id:
                return car
        raise CarNotFoundError(car_id)

    def get_all_cars(self) -> list[Car]:
        """
        Возвращает полный список автомобилей в коллекции.
        
        :return: Список объектов автомобилей.
        """
        return self._cars

    def filter_cars(self, criteria: Callable[[Car], bool]) -> list[Car]:
        """
        Фильтрует коллекцию автомобилей на основе заданного критерия.
        
        :param criteria: Функция-предикат для фильтрации.
        :return: Список автомобилей, соответствующих условию.
        """
        return [car for car in self._cars if criteria(car)]

    def filter_electric_cars(self) -> list[Car]:
        """
        Возвращает только электромобили из коллекции.
        """
        return [c for c in self._cars if isinstance(c, ElectricCar)]

    def search_by_brand(self, brand: str) -> list[Car]:
        """Поиск по марке (без учета регистра)."""
        return [c for c in self._cars if c.brand.lower() == brand.lower()]

    def search_by_model(self, model: str) -> list[Car]:
        """Поиск по модели (без учета регистра)."""
        return [c for c in self._cars if c.model.lower() == model.lower()]

    def filter_by_mileage(self, min_mileage: int) -> list[Car]:
        """Фильтрация по минимальному пробегу."""
        return [c for c in self._cars if c.mileage > min_mileage]

    def sort_cars(self, key_func: Callable[[Car], Any], reverse: bool = False) -> None:
        """
        Выполняет сортировку коллекции автомобилей.
        
        :param key_func: Функция для извлечения ключа сортировки.
        :param reverse: Флаг для сортировки в обратном порядке.
        """
        self._cars.sort(key=key_func, reverse=reverse)

    def save_data(self) -> None:
        """
        Сохраняет текущее состояние коллекции в файл хранилища.
        """
        save_collection(self._cars, self._storage_path)

    def load_data(self) -> None:
        """
        Выполняет перезагрузку данных из файла хранилища.
        """
        self._cars = load_collection(self._storage_path)