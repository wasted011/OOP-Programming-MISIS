from typing import Callable, Any
from models import Car
from exceptions import CarNotFoundError, DuplicateCarError
from storage import save_collection, load_collection

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

    def add_car(self, car: Car) -> None:
        """
        Добавляет новый автомобиль в коллекцию.
        
        :param car: Объект автомобиля для добавления.
        :raises DuplicateCarError: Если автомобиль с таким ID уже существует.
        """
        if any(c.id == car.id for c in self._cars):
            raise DuplicateCarError(car.id)
        self._cars.append(car)

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