<h1 align = 'center' >collection.py</h1>

> В collection.py реализован дата-класс Garage (Коллекция):
> 
> Garage: Коллекция принимает объекты дата-класса Car и реализует различные операции над ними.

## Импорты:

* `validate_mileage` - Валидация атрибута `_mileage` (из Лаб. №1) дата-класса Car (_mileage - type: int, >= 0)

* `validate_class_car` - Валидация объекта дата-класса Car (Объект принадлежит дата-классу Car)

* `validate_index` - Валидация индекса коллекции (index - type: int)

* `validate_reverse` - Валидация значения `reverse` для сортировки (reverse - type: bool)

## Используемые библиотеки:

* `dataclass` - Импорт dataclass (Инициализация type: dataclass объекта), field (Инициализация type: list атрибута дата-класса Garage)

* `datetime` - Импорт date (Инициализация type: date атрибута `_year_of_manufacture` дата-класса Car)

## Дата-класс Garage (Коллекция):

* Инициализация атрибутов коллекции Garage:

  - `_garage` - Контейнер объектов (type: list)

  - `_max_cars` - Максимальное кол-во объектов в контейнере (type: int)

* Создание геттеров для защищенных атрибутов коллекции Garage (Декоратор @property перед каждым геттером):

  - `garage` - Возвращает копию контейнера объектов коллекции Garage

  - `max_cars` - Возвращает максимальное число допустимых объектов коллекции Garage

* Dunder-методы коллекции Garage:

  - `__len__` - Возвращает длину контейнера объектов коллекции Garage
  
  - `__iter__` - Преобразование контейнера объектов type: list в type: iter
  
  - `__getitem__` - Возможность обращаться объекту коллекции Garage по индексу (Также, как и к списку)

* Методы:

  - `add` - Добавление объекта в коллекцию Garage

  - `remove` - Удаление объекта из коллекции Garage (По объекту)

  - `get_all` - Вывод всех объектов коллекции Garage в терминал

  - `find_by_mileage` - Поиск объекта (автомобиля) коллекции Garage по пробегу

  - `remove_at` - Удаление объекта из коллекции Garage (По индексу контейнера type: list)

  - `sort_by_mileage` - Сортировка по пробегу (От меньшего к большему, выбор за пользователем (атрибут: reverse))

  - `sort_by_year_of_manufacture` - Аналогично `sort_by_mileage` только по году выпуска

  - `get_most_used` - Список объектов (автомобилей), чей `_mileage` выше средного по коллекции Garage

  - `get_oldest` - Список объектов (автомобилей), чей `_year_of_manufacture` выше среднего по коллекции Garage

<h1 align = 'center' >model.py</h1>

> В model.py реализована демонастрация дата-класса Garage (Коллекции):
> 
> Базовая демонстрацая (`basic_demonstration`) - Демонстрация методов отдельно друг от друга.
>
> Сценарии (`scenario_*_*****`) - Демонастрация совместно работающих методов в около-реальной работе.

## `basic_demonstraion`:

![basic_demonstration_code](/misc/images/lab_02/basic_demonstraion/basic_demonstration_code.png)

<h1 align = 'center' > ↓ </h1>

![basic_demonstration_terminal](/misc/images/lab_02/basic_demonstraion/basic_demonstration_terminal.png)

## `scenario_1_audit_and_sorting`:

![scenario_01_all_in_all](/misc/images/lab_02/scenarios/scenario_01/scenario_01_all_in_all.png)

<h1 align = 'center' > ↓ </h1>

![scenario_01_terminal](/misc/images/lab_02/scenarios/scenario_01/scenario_01_terminal.png)

## `scenario_2_storage_management`:

![scenario_02_code](/misc/images/lab_02/scenarios/scenario_02/scenario_02_code.png)

<h1 align = 'center' > ↓ </h1>

![scenario_02_terminal](/misc/images/lab_02/scenarios/scenario_02/scenario_02_terminal.png)

## `scenario_3_capacity_control`:

![scenario_03_code](/misc/images/lab_02/scenarios/scenario_03/scenario_03_code.png)

<h1 align = 'center' > ↓ </h1>

![scenario_03_terminal](/misc/images/lab_02/scenarios/scenario_03/scenario_03_terminal.png)
