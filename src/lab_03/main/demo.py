from .models import ElectricCar, SportCar
from src.lab_02.main.collection import Garage

# Создание объектов разных типов (Экземпляров класса):
electric_car_examplar = ElectricCar(brand="Tesla", model="Model 3", year=2022, battery_capacity=100, charge_level=100)
sport_car_examplar = SportCar(brand="Ferrari", model="F40", year=1987, max_speed=324, acceleration=3)

# Вывод объектов
print(electric_car_examplar)
print(sport_car_examplar)

# Использование методов базовых и дочерних классов:
print(electric_car_examplar.recharge(time=30))
print(sport_car_examplar.drive(distance=100))
print(electric_car_examplar.get_service_status())
print(sport_car_examplar.get_service_status())

# Работа с различными типами объектов в коллекции:

garage_examplar = Garage()

# Добавление объектов в гараж:
garage_examplar.add_car(electric_car_examplar)
garage_examplar.add_car(sport_car_examplar)

# Вывод всех объектов в гараже:
print(garage_examplar.get_all_cars())

# Вызов одного метода, разное поведение:

# Для ElectricCar:
print(garage_examplar.get_all_cars()[0].get_service_status())

# Для SportCar:
print(garage_examplar.get_all_cars()[1].get_service_status())

# Единый список объектов разных типов (Через коллекцию):

electric_car_examplar_02 = ElectricCar(brand="Tesla", model="Model S", year=2020, battery_capacity=100, charge_level=100)
sport_car_examplar_02 = SportCar(brand="Ferrari", model="F40", year=1987, max_speed=324, acceleration=3)

garage_examplar.add_car(electric_car_examplar_02)
garage_examplar.add_car(sport_car_examplar_02)

print(garage_examplar.get_all_cars())
# Вызов одинакового метода и получения различных результатов:
print(garage_examplar.get_all_cars()[0].get_service_status())
print(garage_examplar.get_all_cars()[1].get_service_status())
print(garage_examplar.get_all_cars()[2].get_service_status())
print(garage_examplar.get_all_cars()[3].get_service_status())

# Фильтрация объектов по типу:
print(garage_examplar.filter_by_type("ElectricCar"))
print(garage_examplar.filter_by_type("SportCar"))

# Сценарии работы:
# 1. Добавление автомобилей в гараж
# 2. Получение списка всех автомобилей
# 3. Фильтрация по типу автомобиля

# 1. Добавление автомобилей в гараж
garage_examplar.add_car(electric_car_examplar)
garage_examplar.add_car(sport_car_examplar)

# 2. Получения списка всех автомобилей:
print(garage_examplar.get_all_cars())

# 3. Фильтрация по типу автомобиля:
print(garage_examplar.filter_by_type("ElectricCar"))
print(garage_examplar.filter_by_type("SportCar"))