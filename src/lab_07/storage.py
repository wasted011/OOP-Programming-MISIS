import json
from datetime import date
from models import Car, ElectricCar, SportCar

def save_collection(collection: list[Car], filepath: str) -> None:
    """
    Сохраняет коллекцию автомобилей в JSON файл.
    """
    data = [car.to_dict() for car in collection]
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        # Если папка Saved не существует, она должна быть создана вручную 
        # или через системные средства, но здесь мы просто обрабатываем ошибку
        print(f"Ошибка: Директория для файла {filepath} не найдена.")

def load_collection(filepath: str) -> list[list[Car]]:
    """
    Загружает коллекцию автомобилей из JSON файла.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    collection = []
    types_map = {"Car": Car, "ElectricCar": ElectricCar, "SportCar": SportCar}
    
    for item in data:
        try:
            car_type = item.pop("type", "Car")
            if "year_of_manufacture" in item:
                item["year_of_manufacture"] = date.fromisoformat(item["year_of_manufacture"])
            
            cls = types_map.get(car_type, Car)
            collection.append(cls(**item))
        except (KeyError, TypeError, ValueError):
            continue
            
    return collection
