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

<h1 align="center">demo.py</h1>

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

### 1. Полиморфизм: (`scenario_1_polymorphism`)

![scenario_01_code](/misc/images/lab_03/scenarios/scenario_01/scenario_01_code.png)

<p align="center"> ↓ </p>

![scenario_01_terminal](/misc/images/lab_03/scenarios/scenario_01/scenario_01_terminal.png)

### 2. Фильтрация и типы: (`scenario_2_filtering_and_types`)

![scenario_02_code](/misc/images/lab_03/scenarios/scenario_02/scenario_02_code.png)

<p align="center"> ↓ </p>

![scenario_02_terminal](/misc/images/lab_03/scenarios/scenario_02/scenario_02_terminal.png)

### 3. Вместимость и спец. методы: (`scenario_3_inheritance`)

![scenario_03_code](/misc/images/lab_03/scenarios/scenario_03/scenario_03_code.png)

<p align="center"> ↓ </p>

![scenario_03_terminal](/misc/images/lab_03/scenarios/scenario_03/scenario_03_terminal.png)
