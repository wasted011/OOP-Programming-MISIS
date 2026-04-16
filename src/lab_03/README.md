<h1 align = 'center' >models.py</h1>

> В models.py реализовано 2 дочерних класса от Car: ElectricCar и SportCar:
>
> ElectricCar имеет поля: battery_capacity, charge_level
>
> SportCar имеет поля: max_speed, acceleration
>
> Оба класса наследуют все методы и поля от Car, а также добавляют свои уникальные методы и поля.

## Импорты:

### Глобальные:

* `dataclass` - Импорт модуля dataclass.
* `Car` - Импорт класса-родителя Car.

### Локальные:
    
* `validate_type_int` - Ф-ия валидации типа int (type: int).

* `validate_charge_level` - Ф-ия валидации уровня заряда (type: int, range: 0-100).

* `validate_battery_capacity` - Ф-ия валидации емкости батареи (type: int, range: 0-1000).

* `validate_max_speed` - Ф-ия валидации максимальной скорости (type: int, range: 0-1000).

* `validate_acceliration` - Ф-ия валидации ускорения (type: int, range: 0-7).

* `validate_distance` - Ф-ия валидации расстояния (type: int, range: 0-1000).

## Дочерний класс ElectricCar:

### Атрибуты:

* `battery_capacity` - Емкость батареи.

* `charge_level` - Уровень заряда.

### Инкапсуляция:

> Перед каждым геттером декоратор `@property`:
> Сеттер каждого атрибута принимает на вход значение, проходящее валидацию (`validate_*****`) перед присваиванием.

* `battery_capacity` - Геттер и сеттер для емкости батареи.

* `charge_level` - Геттер и сеттер для уровня заряда.

### Методы:

* `recharge` - Метод зарядки электромобиля (Принимает на вход time (время зарядки, type: int) и возвращает строку с информацией о зарядке).

* `drive` - Метод езды на электромобиле (Переопределяет метод родительского класса, добавляет проверку уровня заряда).

* `get_service_status` - Метод получения статуса обслуживания электромобиля (Переопределяет метод родительского класса, добавляет проверку уровня заряда).

## Дочерний класс SportCar:

### Атрибуты:

* `max_speed` - Максимальная скорость.
* `acceleration` - Ускорение.

### Инкапсуляция:

> Перед каждым геттером декоратор `@property`:
> Сеттер каждого атрибута принимает на вход значение, проходящее валидацию (`validate_*****`) перед присваиванием.

* `max_speed` - Геттер и сеттер для максимальной скорости.

* `acceleration` - Геттер и сеттер для ускорения.

### Методы:

* `distance_time` - Метод расчета времени прохождения расстояния (Принимает на вход distance (расстояние, type: int) и возвращает строку с информацией о времени прохождения расстояния).

* `drive` - Метод езды на спорткаре (Переопределяет метод родительского класса, добавляет проверку максимальной скорости).

* `get_service_status` - Метод получения статуса обслуживания спорткара (Переопределяет метод родительского класса, добавляет проверку максимальной скорости).

<<<<<<< HEAD
<h1 align="center">demo.py</h1>
=======
<h1 align = 'center' >demo.py</h1>
>>>>>>> 1d408d7fcdf1edbe4a074bf745bd6e7c2a21913f


> В demo.py реализована демонстрация работы с классами ElectricCar и SportCar:
>
> ElectricCar: Дочерний класс Car (Электромобили).
>
> SportCar: Дочерний класс Car (Спорткары).

## Базовая демонстрация (`basic_demonstration`):

![basic_demonstration_code](/misc/images/lab_03/basic_demonstration/basic_demonstration_code.png)

<p align="center"> ↓ </p>

![basic_demonstration_terminal](/misc/images/lab_03/basic_demonstration/basic_demonstration_terminal.png)

## Сценарии:

### 1. Полиморфизм (`scenario_1_polymorphism`):

![scenario_01_code](/misc/images/lab_03/scenarios/scenario_01/scenario_01_code.png)

<p align="center"> ↓ </p>

![scenario_01_terminal](/misc/images/lab_03/scenarios/scenario_01/scenario_01_terminal.png)


<<<<<<< HEAD
=======
## Вывод всех объектов в гараже:

* `print(garage_examplar.get_all_cars())` - Выводит все объекты в гараже.

## Вызов одного метода, разное поведение:

* `garage_examplar.get_all_cars()[0].get_service_status()` - Получает статус обслуживания первого объекта в гараже.
* `garage_examplar.get_all_cars()[1].get_service_status()` - Получает статус обслуживания второго объекта в гараже.

## Единый список объектов разных типов:

* `garage_examplar.get_all_cars()` - Возвращает список всех объектов в гараже.

## Вызов одинакового метода и получения различных результатов:

* `garage_examplar.get_all_cars()[0].get_service_status()` - Получает статус обслуживания первого объекта в гараже.
* `garage_examplar.get_all_cars()[1].get_service_status()` - Получает статус обслуживания второго объекта в гараже.
* `garage_examplar.get_all_cars()[2].get_service_status()` - Получает статус обслуживания третьего объекта в гараже.
* `garage_examplar.get_all_cars()[3].get_service_status()` - Получает статус обслуживания четвертого объекта в гараже.

## Фильтрация объектов по типу:

* `garage_examplar.filter_by_type("ElectricCar")` - Возвращает список объектов типа ElectricCar.
* `garage_examplar.filter_by_type("SportCar")` - Возвращает список объектов типа SportCar.

## Сценарии работы:

* Добавление автомобилей в гараж:
  * `garage_examplar.add_car(electric_car_examplar)`
  * `garage_examplar.add_car(sport_car_examplar)`
* Получение списка всех автомобилей:
  * `garage_examplar.get_all_cars()`
* Фильтрация по типу автомобиля:
  * `garage_examplar.filter_by_type("ElectricCar")`
  * `garage_examplar.filter_by_type("SportCar")`
>>>>>>> 1d408d7fcdf1edbe4a074bf745bd6e7c2a21913f
