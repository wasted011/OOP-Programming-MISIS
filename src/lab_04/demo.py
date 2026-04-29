from datetime import date
from .realization import Car, Garage, ElectricCar, proccess_car
from .interfaces import Printable

def print_info(obj: Printable):
    print(obj.get_info())

def for_three():
    
    # Инициализация объектов разных типов:

    example_car_object = Car(_brand="Toyota", _model="Camry", _mileage=50000, _year_of_manufacture=date(2020, 1, 1))
    example_garage_object = Garage()
    example_electric_car_object = ElectricCar(_brand="Tesla", _model="Model 3", _mileage=30000, _year_of_manufacture=date(2021, 6, 15))

    # Вызов методов интерфейса:

    print(f"Car service status: {example_car_object.get_service_status()}")
    print(f"Garage cars: {example_garage_object.get_all()}")
    print(f"Electric car charge: {example_electric_car_object.charge(time=120)}")

    # Разное поведение у разных классов:
    
    # 1. Метод drive в ванильном Car:

    print(f"Car drive result: {example_car_object.drive(distance=1000)}")

    # 2. Метод drive в дочерке ElectricCar:

    print(f"Electric car drive result: {example_electric_car_object.drive(distance=1000)}")

def for_four():
    
    # Работа ф-ии, работающей с разными объектами через интерфейс:

    car = Car(_brand="BMW", _model="X5", _mileage=0, _year_of_manufacture=date(2022, 3, 10))
    garage = Garage()
    electric_car = ElectricCar(_brand="Tesla", _model="Model S", _mileage=0, _year_of_manufacture=date(2023, 1, 1))
    
    print_info(car)
    print_info(garage)
    print_info(electric_car)
    
    # isinstance использован в ф-иях валидации.

    # Демонстрация, что объект использует разные интерфейсы:

    print(f"Car MRO: {Car.__mro__}")
    print(f"Garage MRO: {Garage.__mro__}")
    print(f"ElectricCar MRO: {ElectricCar.__mro__}")

def for_five():

    # Единый список объектов разных типов:

    objects = [
        Car(_brand="Ford", _model="Focus", _mileage=0, _year_of_manufacture=date(2019, 5, 20)),
        Garage(),
        ElectricCar(_brand="Nissan", _model="Leaf", _mileage=0, _year_of_manufacture=date(2022, 11, 30))
    ]
    
    # Вывод их в терминал:
    print("--- Вывод информации о всех объектах коллекции ---")
    for obj in objects:
        print_info(obj)

    # Сценарии работы (около-реальные):

    # - 1. Вывод информации о всех объектах коллекции:

    print("--- Полиморфное поведение объектов ---")
    for obj in objects:
        if isinstance(obj, Car):
            print(f"Service status: {obj.get_service_status()}")
        elif isinstance(obj, Garage):
            print(f"Garage info: {obj.get_all()}")
    
    # - 3. Вывод информации о объектах, принадлежащих к определенному интерфейсу:
    
    print("--- Объекты, принадлежащие интерфейсу Printable ---")
    for obj in objects:
        if isinstance(obj, Printable):
            print_info(obj)
    
if __name__ == "__main__":
    for_five()