from .realization import Car, Garage, ElectricCar

def for_three():
    
    # Инициализация объектов разных типов:

    example_car_object = Car()
    example_garage_object = Garage()
    example_electric_car_object = ElectricCar()

    # Вызов методов интерфейса:

    example_car_object.get_service_status()
    example_garage_object.get_all()
    example_electric_car_object.charge()

    # Разное поведение у разных классов:
    
    # 1. Метод drive в ванильном Car:

    print(example_car_object.drive(distance=1000))

    # 2. Метод drive в дочерке ElectricCar:

    print(example_electric_car_object.drive(distance=1000))

def for_four():

    # Работа ф-ии, работающей с разными объектами через интерфейс:

    def print_info(obj: Printable):
        print(obj.print_info())
    
    print_info(Car())
    print_info(Garage())
    print_info(ElectricCar())
    
    # isinstance использован в ф-иях валидации.

    # Демонстрация, что объект использует разные интерфейсы:

    print(Car().__class__.__mro__)
    print(Garage().__class__.__mro__)
    print(ElectricCar().__class__.__mro__)

def for_five():

    # Единый список объектов разных типов:

    objects = [Car(), Garage(), ElectricCar()]
    
    # Вывод их в терминал:
    for obj in objects:
        print_info(obj)

    # Сценарии работы (около-реальные):

    # - 1. Вывод информации о всех объектах коллекции:

    for obj in objects:
        print_info(obj)

    # - 2. Полиморфное поведение объектов:

    for obj in objects:
        obj.get_service_status()
    
    # - 3. Вывод информации о объектах, принадлежащих к определенному интерфейсу:
    
    for obj in objects:
        if isinstance(obj, Printable):
            print_info(obj)
    
if __name__ == "__main__":
    for_three()