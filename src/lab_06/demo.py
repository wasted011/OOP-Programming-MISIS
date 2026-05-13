from .container import TypedCollection, T, D, Sc
from .validate import *
from src.lab_03.main.base import Car
from src.lab_03.main.models import ElectricCar, SportCar
from datetime import date

# Создание типизированной коллекции и добавление объектов:

typed_collection_example: TypedCollection[T] = TypedCollection[T]()

# Инициализация объектов:

object_example_01 = Car(_brand="Toyota", _model="Camry", _mileage=50000, _year_of_manufacture=date(2020, 1, 1))
object_example_02 = Car(_brand="Honda", _model="Civic", _mileage=60000, _year_of_manufacture=date(2019, 1, 1))
object_example_03 = Car(_brand="Ford", _model="Focus", _mileage=70000, _year_of_manufacture=date(2018, 1, 1))

# Добавление объектов в коллекцию:

typed_collection_example.add(object_example_01)
typed_collection_example.add(object_example_02)
typed_collection_example.add(object_example_03)


def for_three():
    
    # Демонстрация валидации типов при добавлении объекта другого типа:
    print("Попытка добавления объекта некорректного типа (строки):")
    try:
        typed_collection_example.add("not a car")
    except TypeError as e:
        print(f"Error: {e}")
    
    # Получение всех элементов и вывод каждого:
    all_elements = typed_collection_example.get_all()
    print(f"Все элементы: {all_elements}")

    for obj in all_elements:
        print(obj)

def for_four():
    
    # Вызов find_by():
    print("Вызов find_by():")
    found = typed_collection_example.find_by(lambda x: hasattr(x, '_brand') and x._brand == "Toyota")
    print(f"Найден элемент: {found}")
    
    not_found = typed_collection_example.find_by(lambda x: hasattr(x, '_brand') and x._brand == "BMW")
    print(f"Элемент не найден: {not_found}")

    # Вызов filter_by():
    print("\nВызов filter_by():")
    filtered = typed_collection_example.filter_by(lambda x: hasattr(x, '_year_of_manufacture') and x._year_of_manufacture.year > 2018)
    print(f"Отфильтрованные элементы: {filtered}")

    # Вызов map_by():
    print("\nВызов map_by():")
    # - 1-ая Ф-ия (бренды):
    mapped_brands = typed_collection_example.map_by(lambda x: x._brand + "!" if hasattr(x, '_brand') else str(x) + "!")
    print(f"Отображенные бренды: {mapped_brands}")

    # - 2-ая Ф-ия (пробег):
    mapped_mileage = typed_collection_example.map_by(lambda x: x._mileage + 10000 if hasattr(x, '_mileage') else 10000)
    print(f"Отображенный увеличенный пробег: {mapped_mileage}")

def for_five():
    
    print("Сценарий №1: TypedCollection[D] (Displayable - требует get_service_status)")
    
    # Создаем коллекцию для любых объектов Car, которые мы будем трактовать как Displayable
    displayable_collection: TypedCollection[Car] = TypedCollection[Car]()
    
    car1 = ElectricCar(_brand="Tesla", _model="Model S", _mileage=1000, _year_of_manufacture=date(2022, 5, 10))
    car2 = SportCar(_brand="Ferrari", _model="F40", _mileage=5000, _year_of_manufacture=date(1990, 1, 1), _max_speed=324, _acceleration=4)
    
    displayable_collection.add(car1)
    displayable_collection.add(car2)
    
    print("Статус обслуживания объектов в коллекции:")
    for item in displayable_collection.get_all():
        print(f"{item._brand}: {item.get_service_status()}")

    print("\nСценарий №2: Работа с протоколом Scorable (recharge)")
    
    # Создаем коллекцию специально для электромобилей
    scorable_collection: TypedCollection[ElectricCar] = TypedCollection[ElectricCar]()
    
    e_car1 = ElectricCar(_brand="Nissan", _model="Leaf", _mileage=15000, _year_of_manufacture=date(2021, 3, 15))
    e_car2 = ElectricCar(_brand="Tesla", _model="Model 3", _mileage=5000, _year_of_manufacture=date(2023, 1, 1))
    
    scorable_collection.add(e_car1)
    scorable_collection.add(e_car2)
    
    print("Зарядка электромобиля e_car1:")
    print(e_car1.recharge(50))

    print("\nСценарий №3: Массовое применение операции (apply) к Scorable объектам")
    # Демонстрируем метод apply для выполнения действия над всеми элементами коллекции
    print("Заряжаем все электромобили в scorable_collection на 100 единиц времени:")
    scorable_collection.apply(lambda x: print(f"Результат для {x._brand}: {x.recharge(100)}"))

if __name__ == "__main__":
    for_five()