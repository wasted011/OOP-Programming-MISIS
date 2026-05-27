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
    app.add_car(Car(1, "Toyota", "Corolla", 15000, date(2021, 5, 20)))
    app.add_car(Car(2, "Honda", "Civic", 22000, date(2020, 3, 15)))
    
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
    app.add_car(ElectricCar(10, "Tesla", "Model 3", 5000, date(2022, 1, 1), 75, 100))
    
    print("Шаг 2: Тестирование поиска по марке 'Tesla'...")
    results = app.filter_cars(lambda c: c.brand.lower() == "tesla")
    for car in results:
        print(f"Найдено: {car}")
        
    print("\nШаг 3: Демонстрация перехвата DuplicateCarError (ID: 10)...")
    try:
        app.add_car(Car(10, "Audi", "A4", 10000, date(2021, 1, 1)))
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
    app_save.add_car(SportCar(50, "Ferrari", "F8", 1000, date(2023, 1, 1), 340, 2.9))
    app_save.save_data()
    
    print("\nШаг 2: Симуляция перезапуска и автоматической загрузки...")
    app_load = CarApp(storage_path=storage_path)
    for car in app_load.get_all_cars():
        print(f"Загружено из файла: {car}")
        
    print("\nШаг 3: Демонстрация сортировки по возрастанию пробега...")
    app_load.add_car(Car(51, "Lada", "Vesta", 30000, date(2018, 1, 1)))
    app_load.sort_cars(lambda c: c.mileage)
    for car in app_load.get_all_cars():
        print(f"В списке: {car}")

if __name__ == "__main__":
    for_five()