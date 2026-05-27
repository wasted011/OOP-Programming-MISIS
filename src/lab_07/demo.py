import sys
from datetime import date

# Прямое добавление текущей директории для импортов
sys.path.append(".")

from app import CarApp
from models import Car, ElectricCar, SportCar
from exceptions import DuplicateCarError, CarNotFoundError

def for_three() -> None:
    """
    Демонстрация базового функционала приложения (Оценка 3).
    """
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦИЯ: БАЗОВЫЕ СЦЕНАРИИ (ОЦЕНКА 3)")
    print("="*50)

    # Путь задается строкой относительно корня lab_07
    storage_path = "Saved/demo_grade_3.json"
    app = CarApp(storage_path=storage_path)
    # Очистка коллекции перед началом для предотвращения ошибок при повторном запуске
    app._cars = []

    print("\nШаг 1: Добавление стандартных автомобилей в коллекцию...")
    app.add_car("standard", id=1, brand="Toyota", model="Corolla", mileage=15000, year_of_manufacture=2021)
    app.add_car("standard", id=2, brand="Honda", mileage=22000, model="Civic", year_of_manufacture=2020)
    
    print("Список в памяти:")
    for car in app.get_all_cars():
        print(f"Запись: {car}")

    print("\nШаг 2: Сохранение данных на диск...")
    app.save_data()
    print("Результат: Файл сохранен в Saved/demo_grade_3.json")

def for_four() -> None:
    """
    Демонстрация работы с исключениями и фильтрацией (Оценка 4).
    """
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦИЯ: НЕОБЫЧНЫЕ СЦЕНАРИИ (ОЦЕНКА 4)")
    print("="*50)

    storage_path = "Saved/demo_grade_4.json"
    app = CarApp(storage_path=storage_path)
    
    print("\nШаг 1: Наполнение коллекции объектами разных типов...")
    app._cars = [] 
    app.add_car("electric", id=10, brand="Tesla", model="Model 3", mileage=5000, year_of_manufacture=2022, battery_capacity=75, charge_level=100)
    
    print("Шаг 2: Тестирование поиска по марке 'Tesla'...")
    results = app.search_by_brand("Tesla")
    for car in results:
        print(f"Найдено: {car}")
        
    print("\nШаг 3: Демонстрация перехвата DuplicateCarError (ID: 10)...")
    try:
        app.add_car("standard", id=10, brand="Audi", model="A4", mileage=10000, year_of_manufacture=2021)
    except DuplicateCarError as e:
        print(f"Информационное сообщение: {e}")

def for_five() -> None:
    """
    Демонстрация расширенных возможностей приложения (Оценка 5).
    """
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦИЯ: РАСШИРЕННЫЕ СЦЕНАРИИ (ОЦЕНКА 5)")
    print("="*50)

    storage_path = "Saved/demo_grade_5.json"
    
    print("\nШаг 1: Создание SportCar и сохранение состояния...")
    app_save = CarApp(storage_path=storage_path)
    app_save._cars = []
    app_save.add_car("sport", id=50, brand="Ferrari", model="F8", mileage=1000, year_of_manufacture=2023, max_speed=340, acceleration=2.9)
    app_save.save_data()
    
    print("\nШаг 2: Симуляция перезапуска и автоматической загрузки...")
    app_load = CarApp(storage_path=storage_path)
    for car in app_load.get_all_cars():
        print(f"Загружено из файла: {car}")
        
    print("\nШаг 3: Демонстрация сортировки по возрастанию пробега...")
    app_load.add_car("standard", id=51, brand="Lada", model="Vesta", mileage=30000, year_of_manufacture=2018)
    app_load.sort_cars(lambda c: c.mileage)
    for car in app_load.get_all_cars():
        print(f"В списке: {car}")

if __name__ == "__main__":
    for_three()
    for_four()
    for_five()