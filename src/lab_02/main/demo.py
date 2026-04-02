from .collection import Garage
from src.lab_01.main.model import Car
from datetime import date

# Инициализация тестовых объектов (test_objcet_01, test_object_02):

test_object_01 = Car("Toyota", "Camry", 2000, date(2015, 1, 1))
test_object_02 = Car("Toyota", "Corolla", 1000, date(2014, 1, 1))

# Инициализация экземляра класса Garage - test_garage:

test_garage = Garage()

# Добавление объектов в коллекцию (В экземпляр класса Garage - test_garage):
test_garage.add_car(new_object=test_object_01)
test_garage.add_car(new_object=test_object_02)

# Вывод всех элементов экземпляра класса Garage - test_garage:

print(test_garage.get_all())

# Удаление элемента из коллекции:

test_garage.delete_car(car_id=1)

# Повторный вывод коллекции:

print(test_garage.get_all())

# Метод find_by_*** (find_by_id()):

print(test_garage.find_by_id(0))

#smth