from datetime import date
from src.lab_02.main.collection import Garage
from src.lab_01.main.model import Car

def basic_demonstration():

    # 1. Инициализация нескольких объектов:
    car_a = Car("Toyota", "Camry", 50000, date(2015, 1, 1))
    car_b = Car("Honda", "Civic", 20000, date(2018, 1, 1))
    car_c = Car("Lada", "Vesta", 80000, date(2012, 1, 1))
    
    garage = Garage()
    
    # 2. Добавление их в коллекцию:

    garage.add(car_a)
    garage.add(car_b)
    garage.add(car_c)
    
    # 3. Использование len():
    print(f"Количество машин в коллекции (через len): {len(garage)}")

    # 4. Вывод всех элементов (использование цикла for):
    for car in garage:
        print(car)
        
    # 5. Поиск элемента
    print(f"Поиск машины по пробегу 20000: {garage.find_by_mileage(20000)}")
    
    # 6. Работа ограничения на дубликаты:
    print(f"Попытка добавить дубликат Toyota: {garage.add(car_a)}") # Ожидается False
    
    # 7. Удаление элемента:
    print(f"Удаление объекта Honda: {garage.remove(car_b)}")
    
    # 8. Повторный вывод коллекции:
    print(f"Коллекция после удаления: {garage.get_all()}")

# Сценарий 1: Технический аудит автопарка (Сортировка и Фильтрация).

def scenario_1_audit_and_sorting():

    # Создания экземпляра коллекции Garage:
    fleet = Garage()

    # Инициализация объектов класса Car в коллекцию:
    fleet.add(Car("BMW", "X5", 10000, date(2022, 1, 1)))
    fleet.add(Car("Audi", "A6", 120000, date(2010, 1, 1)))
    fleet.add(Car("Tesla", "Model 3", 5000, date(2023, 1, 1)))
    
    # Демонстрация сортировки:
    fleet.sort_by_mileage(reverse=True)

    # Сортировка по пробегу (От меньшего к большему):
    for car in fleet: print(f"{car.brand}: {car.mileage}")
    
    # Демонстрация фильтрации
    
    # Фильтрация автомобилей с пробегом выше среднего:
    for car in fleet.get_most_used(): 
        print(f"Требует ТО: {car}")

# Сценарий 2: Управление хранилищем (Индексация).

def scenario_2_storage_management():

    # Создания экземпляра коллекции Garage:
    storage = Garage()

    # Инициализация объектов класса Car в коллекцию:
    storage.add(Car("Porsche", "911", 5000, date(2023, 1, 1)))
    storage.add(Car("Ferrari", "F40", 1200, date(1990, 1, 1)))
    
    # Демонстрация индексации:
    print(f"Машина в ячейке №0: {storage[0]}")
    print(f"Машина в ячейке №1: {storage[1]}")
    
    # Демонстрация удаления по индексу:
    storage.remove_at(0)
    print(f"Теперь в ячейке №0 находится: {storage[0]}")

# Сценарий 3: Контроль вместимости и безопасности.

def scenario_3_capacity_control():

    # Инициализация объектов класса Car в коллекцию:
    secure_garage = Garage(_max_cars=2)
    
    # Инициализация объектов класса Car в коллекцию:

    secure_garage.add(Car("Volvo", "XC90", 10000, date(2021, 1, 1)))
    secure_garage.add(Car("Mercedes", "S-Class", 30000, date(2020, 1, 1)))
    
    # Демонстрация ограничения коллекции:

    try:
        secure_garage.add(Car("Ford", "Focus", 80000, date(2015, 1, 1)))
    except IndexError:
        print("Свободных мест нет") # Поднимается IndexError.
    
    print(f"В итоге в гараже: {secure_garage.get_all()}")

# Точка входа в программу
if __name__ == "__main__":
    basic_demonstration()
    scenario_1_audit_and_sorting()
    scenario_2_storage_management()
    scenario_3_capacity_control()
