from datetime import date
from src.lab_03.main.models import ElectricCar, SportCar
from src.lab_02.main.collection import Garage

def basic_demonstration():
    
    # 1. Создание объектов разных типов:
    ecar = ElectricCar(_brand="Tesla", _model="Model 3", _mileage=5000, _year_of_manufacture=date(2022, 1, 1), _battery_capacity=100, _charge_level=50)
    scar = SportCar(_brand="Ferrari", _model="F40", _mileage=1000, _year_of_manufacture=date(1990, 1, 1), _max_speed=324, _acceleration=3)
    
    # 2. Вывод объектов:
    print(f"Электромобиль: {ecar}")
    print(f"Спорткар: {scar}")
    
    # 3. Использование методов базового и дочернего класса:
    print(f"Статус обслуживания (Tesla, base): {ecar.get_service_status()}")
    print(f"Зарядка (Tesla, child): {ecar.recharge(time=20)}")
    
    print(f"Статус обслуживания (Ferrari, base): {scar.get_service_status()}")
    print(f"Время проезда дистанции (Ferrari, child): {scar.distance_time(distance=100)}")

def scenario_1_polymorphism():
    
    # Работа с разными типами через одну коллекцию:
    fleet = Garage()
    
    # Добавление разных типов в одну коллекцию:
    fleet.add(ElectricCar(_brand="Nissan", _model="Leaf", _mileage=20000, _year_of_manufacture=date(2019, 5, 10), _battery_capacity=40, _charge_level=15)) # Low charge
    fleet.add(SportCar(_brand="Porsche", _model="911", _mileage=110000, _year_of_manufacture=date(2015, 3, 15), _max_speed=300, _acceleration=4)) # High mileage
    fleet.add(ElectricCar(_brand="Tesla", _model="Model S", _mileage=10000, _year_of_manufacture=date(2021, 1, 1), _battery_capacity=100, _charge_level=80))
    
    # Вызов одного метода (get_service_status) — разное поведение (Метод переопределен в ElectricCar и SportCar):
    for car in fleet:
        print(f"Машина: {car.brand} {car.model}, Пробег: {car.mileage}, Статус: {car.get_service_status()}")

def scenario_2_filtering_and_types():
    
    garage = Garage()
    garage.add(ElectricCar(_brand="Tesla", _model="Model X", _mileage=5000, _year_of_manufacture=date(2022, 1, 1), _battery_capacity=100, _charge_level=100))
    garage.add(SportCar(_brand="Lamborghini", _model="Aventador", _mileage=2000, _year_of_manufacture=date(2021, 1, 1), _max_speed=350, _acceleration=2))
    
    # Единый список объектов разных типов:
    print(f"Всего машин в коллекции: {len(garage)}")
    
    # Фильтрация по типу через метод коллекции:
    print("Только электромобили:")
    for car in garage.get_vehicle_by_type(ElectricCar):
        print(f" - {car}")
        
    # Проверка типов через isinstance():
    print("Проверка типов через isinstance():")
    for car in garage:
        if isinstance(car, ElectricCar):
            print(f"{car.brand} {car.model} - это ElectricCar")
        elif isinstance(car, SportCar):
            print(f"{car.brand} {car.model} - это SportCar")

def scenario_3_capacity_and_specifics():
    
    # Контроль вместимости:
    secure_garage = Garage(_max_cars=2)
    ecar = ElectricCar(_brand="Audi", _model="e-tron", _mileage=10000, _year_of_manufacture=date(2020, 1, 1), _battery_capacity=95, _charge_level=10)
    scar = SportCar(_brand="Bugatti", _model="Chiron", _mileage=500, _year_of_manufacture=date(2022, 1, 1), _max_speed=420, _acceleration=2)
    
    secure_garage.add(ecar)
    secure_garage.add(scar)
    
    # Демонстрация ограничения коллекции:
    print(f"Машин в гараже: {len(secure_garage)}")
    try:
        print("Попытка добавить третью машину...")
        secure_garage.add(ElectricCar(_brand="BMW", _model="i3", _mileage=0, _year_of_manufacture=date(2023, 1, 1), _battery_capacity=40, _charge_level=100))
    except IndexError:
        print("Ошибка: Свободных мест нет!")
        
    # Вызов специфических методов в зависимости от типа:
    print("Выполнение специфических действий для каждой машины:")
    for car in secure_garage:
        if isinstance(car, ElectricCar):
            print(f"{car.brand}: Зарядка... {car.recharge(30)}")
        elif isinstance(car, SportCar):
            print(f"{car.brand}: Расчет времени на 200км... {car.distance_time(200)}")

# Точка входа в программу
if __name__ == "__main__":
    basic_demonstration()
    scenario_1_polymorphism()
    scenario_2_filtering_and_types()
    scenario_3_capacity_and_specifics()
