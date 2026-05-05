
from .collection import Garage
from .strategies import *

# Создание коллекции:

test_collection = Garage()

# Инициализация объектов коллекции (5 шт.):

test_collection.add(Car("Toyota", "Camry", 50000, date(2020, 1, 1)))
test_collection.add(Car("Honda", "Civic", 60000, date(2019, 1, 1)))
test_collection.add(Car("Ford", "Focus", 70000, date(2018, 1, 1)))
test_collection.add(Car("BMW", "X5", 80000, date(2017, 1, 1)))
test_collection.add(Car("Audi", "A4", 90000, date(2016, 1, 1)))

def for_three():

    # Сортировка коллекции 3 разными стратегиями:

    print("======== Сортировка по бренду ========")

    result = sorted(test_collection, key=sort_by_brand)

    for obj in result:
        print(f"{obj._brand} {obj._model} {obj._mileage} {obj._year_of_manufacture}")

    print("======== Сортировка по модели ========")

    result = sorted(test_collection, key=sort_by_model)

    for obj in result:
        print(f"{obj._brand} {obj._model} {obj._mileage} {obj._year_of_manufacture}")

    print("======== Сортировка по пробегу ========")

    result = sorted(test_collection, key=sort_by_mileage)

    for obj in result:
        print(f"{obj._brand} {obj._model} {obj._mileage} {obj._year_of_manufacture}")

    # Фильтрация коллекции 2 разными функциями-фильтрами:

    print("======== Фильтрация по бренду ========")

    result = list(filter(filter_by_brand, test_collection))

    for obj in result:
        print(f"{obj._brand} {obj._model} {obj._mileage} {obj._year_of_manufacture}")

    print("======== Фильтрация по модели ========")

    result = list(filter(filter_by_model, test_collection))

    for obj in result:
        print(f"{obj._brand} {obj._model} {obj._mileage} {obj._year_of_manufacture}")

def for_four():

    print("======== Применение метода map ========")

    print("До:")
    for obj in test_collection:
        print(f"{obj._model}: {obj._mileage};", end = " ")
    
    result = list(map(add_mileage, test_collection))

    print("\nПосле:")
    for obj in test_collection:
        print(f"{obj._model}: {obj._mileage};", end = " ")

    print("\n======== Использование фабрики функций ========")

    print("До:")
    for obj in test_collection:
        print(f"{obj._model}", end = " ")
    print(f"\nКол-во машин до: {len(test_collection)}")
    
    print("\nПосле:")
    result = list(filter(filter_by_mileage_fabric(50000), test_collection))
    for obj in result:
        print(f"{obj._model}", end = " ")
    print(f"\nКол-во машин после: {len(result)}")

    print("\n======== Вызов методов sort_by()/filter_by() коллекции ========")

    print("\nСортировка по пробегу")

    result = test_collection.sort_by(key=sort_by_mileage)

    for obj in result:
        print(f"{obj._model}: {obj._mileage}")

    print("\nФильтрация по пробегу")
    
    result = test_collection.filter_by(predicate=filter_by_mileage)
    for obj in result:
        print(f"{obj._model}: {obj._mileage}")

    print("\n======== Сравнение: один и тот же результат через lambda и через именованную функцию ========")

    print(f"Сравнение результатов (True - если все верно): {list(filter(lambda car: car._mileage <= 50000, test_collection)) == list(filter(filter_by_mileage, test_collection))}")

def for_five():

    print("======== Сценарий 1: полная цепочка filter → sort → apply с выводом на каждом шаге ========")

    print("До применения:")
    for obj in test_collection:
        print(obj)
    
    print("После применения filter → sort → apply:")
    result_01 = (test_collection
        .filter_by(predicate=filter_by_mileage)
        .sort_by(key=sort_by_mileage)
        .apply(operation=apply_mileage_increase)
    )

    for obj in result_01:
        print(obj)

    print("======== Сценарий 2: замена стратегии без изменения кода коллекции — показать, что при передаче другой функции результат меняется ========")

    # - Применение первой стратегии:

    print("До применения первой стратегии:")
    
    for obj in test_collection:
        print(obj)

    print("После применения первой стратегии:")
    result_02 = test_collection.apply(operation=apply_mileage_increase)
    for obj in result_02:
        print(obj)

    # - Применение второй стратегии:

    print("До применения второй стратегии:")
    for obj in test_collection:
        print(obj)

    result_03 = test_collection.apply(operation=apply_mileage_decrease)

    print("После применения второй стратегии:")
    for obj in result_03:
        print(obj)

    print(f"Сравнение результатов (True - если все верно): {result_02 != result_03}")

    print("======== Сценарий 3: демонстрация callable-объекта как стратегии: (Вообще реализованно выше, но все же) ========")

    print("До применения callable-объекта:")
    for obj in test_collection:
        print(obj)
    
    class MileageMultiplier:
        
        def __call__(self, car):
            car._mileage *= 1.5
            return car
    
    multiplier = MileageMultiplier()
    result_04 = test_collection.apply(operation=multiplier)

    print("После применения callable-объекта:")
    for obj in result_04:
        print(obj)

if __name__ == "__main__":
    for_three()
    for_four()
    for_five()
    