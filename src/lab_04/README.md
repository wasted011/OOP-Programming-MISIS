<h1 align="center">interfaces.py</h1>

> В interfaces.py реализованы интерфейсы CarInterface, GarageInterface и их реализации Printable.

# CarInterface:

* Абстрактные атрибуты (`@property` с флагом `@abstractmethod`):

  * `brand` - Бренд автомобиля (type: str) (Контракт наличия геттера)

  * `model` - Модель автомобиля (type: str) (Контракт наличия геттера)

  * `mileage` - Пробег автомобиля (type: int) (Контракт наличия геттера)

  * `year_of_manufacture` - Год выпуска автомобиля (type: date) (Контракт наличия геттера)

* Абстрактные методы (`@abstractmethod`):

  * `get_service_status()` - Проверка состояния автомобиля (type: bool)

  * `drive(distance: int)` - Пробег автомобиля (type: int)

# GarageInterface:

* Абстрактные атрибуты (`@property` с флагом `@abstractmethod`):

  * `garage` - Гараж (type: list[CarInterface]) (Контракт наличия геттера)

* Абстрактные методы (`@abstractmethod`):

  * `max_cars()` - Максимальное количество автомобилей (type: int)

  * `add(car: CarInterface)` - Добавление автомобиля (type: bool)

  * `remove(car: CarInterface)` - Удаление автомобиля (type: bool)

  * `remove_at(index: int)` - Удаление автомобиля по индексу (type: bool)

  * `get_all()` - Получение всех автомобилей (type: list[CarInterface])

# Printable:

* Абстрактный метод (`@abstractmethod`):

  * `print_info()` - Печать информации об автомобиле (type: None)

<h1 align="center">realization.py</h1>

> В realization.py созданы классы Car, Garage и Printable, которые реализуют интерфейсы из interfaces.py.

# Car (Наследует от CarInterface и Printable):

* Атрибуты:

  * `_brand` - Бренд автомобиля (type: str)

  * `_model` - Модель автомобиля (type: str)

  * `_mileage` - Пробег автомобиля (type: int)

  * `_year_of_manufacture` - Год выпуска автомобиля (type: date)

* Геттеры и сеттеры:

> После всех геттеров, идут сеттеры, значение которых проходит `validate_****` перед присваиванием.

  * `brand` - Геттер атрибута `_brand`

  * `model` - Геттер атрибута `_model`

  * `mileage` - Геттер атрибута `_mileage`

  * `year_of_manufacture` - Геттер атрибута `_year_of_manufacture`

* Методы:

  * `get_service_status()` - Проверка состояния автомобиля (type: bool)

  * `drive(distance: int)` - Пробег автомобиля (type: int)

  * `get_info()` - Печать информации об автомобиле (type: None)

# Универсальная функция:

* Функция `proccess_car(obj: Printable) -> str` - Универсальная функция, работающая через интерфейс Printable.

# Garage (Наследует от GarageInterface):

* Атрибуты:

  * `_garage` - Гараж (type: list[CarInterface])

  * `_max_cars` - Максимальное количество автомобилей (type: int)

* Геттеры и сеттеры:

  * `garage` - Геттер атрибута `_garage`

  * `max_cars` - Геттер атрибута `_max_cars`

* Методы:

  * `add(car: CarInterface)` - Добавление автомобиля (type: bool)

  * `remove(car: CarInterface)` - Удаление автомобиля (type: bool)

  * `remove_at(index: int)` - Удаление автомобиля по индексу (type: bool)

  * `get_all()` - Получение всех автомобилей (type: list[CarInterface])

  * `filter_by_interface(interface_type: type)` - Фильтрация объектов коллекции по интерфейсу (type: list[CarInterface | GarageInterface])

  * `sort_by_mileage()` - Сортировка автомобилей по пробегу (type: list[CarInterface])

# ElectricCar (Наследует от Car):

* Атрибуты:

  * `_battery_capacity` - Емкость батареи (type: int)

  * `_charge_level` - Уровень заряда (type: int)

* Геттеры и сеттеры:

  * `battery_capacity` - Геттер атрибута `_battery_capacity`

  * `charge_level` - Геттер атрибута `_charge_level`

* Методы:

  * `charge(time: int)` - Зарядка автомобиля (type: int)

  * `drive(distance: int)` - Пробег автомобиля (type: tuple[int, int])

<h1 align="center">demo.py</h1>

> В demo.py продемонстрировано использование интерфейсов и классов.

# for_three:

![for_three_code](/misc/images/lab_04/for_three/for_three_code.png)

# for_four:

![for_four_code](/misc/images/lab_04/for_four/for_four_code.png)

# for_five:

![for_five_code](/misc/images/lab_04/for_five/for_five_code.png)
