<h1 align = 'center' >model.py</h1>

> В model.py реализованно 2 дата-класса (Car и CarFuncs):
> 
> Car: Инициализирует всю первичную информацию о автомобиле (Прозводитель, модель и т. д.).
> 
> CarFuncs: Основные функции автомобиля (Вкл/Выкл фар/сигналов и т. д.).

## Дата-класс Car:

* ### Инициализация дата-класса Car и его атрибутов:
  
  - `_brand` - Бренд автомобиля.
    
  - `_model` - Модель автомобиля.
    
  - `_mileage` - Пробег автомобиля.
    
  - `year_of_manufacture` - Год выпуска автомобиля.

* ### Создание геттеров и сеттеров для защищенных атрибутов (_variable) дата-класса Car:
  
  - `@property` (Перед каждым сеттером ниже, возвращает защищенный атрибут (Геттер)):
  - В каждом сеттер значение проходит валидацию `validate_car_*****` перед присваиванием:
    
     - `brand.setter` - Сеттер защищенного атрибута `_brand`.
       
     - `model.setter` - Сеттер защищенного атрибута `_model`.
       
     - `mileage.setter` - Сеттер защищенного атрибута `_mileage`.
       
     - `year_of_manufacture.setter` - Сеттер защищенного атрибута `_year_of_manufacture`.
      
* ### Валидация атрибутов дата-класса Car:
  
  - `validate_car_brand` - Валидация бренда автомобиля (Бренд - str, Бренд != пустой строке).
    
  - `validate_car_model` - Валидация модели автомобиля (Модель - str, Модель != пустой строке).
    
  - `validate_car_mileage` - Валидация пробега автомобиля (Пробег - int, Пробег >= 0).
    
  - `validate_year_of_manufacture` - Валидация даты выпуска автомобиля (Дата - type: date, Дата выпуска >= Дата сегодня).

* ### Реализация Dunder-методов дата-класса Car:

  - `__str__` - Красивый вывод атрибутов объекта дата-класса Car (`_brand`, `_model` и т.д.)
  - `__repr__` - Практически идентичен с `__str__`, разница в формате вывода (Бренд: `self._brand` - brand= `self._brand`).
  - `__eq__` - Метод сравнения двух объектов (Объекты равны при равенстве всех атрибутов (self.brand == other.brand и т.д.)

## Дата-класс CarFuncs:

* ### Инициализация дата-класса CarFuncs и его атрибутов:
  
  - `_car` - Объект дата-класса Car.
    
  - `engine` - Состояние двигателя автомобиля.
    
  - `lights` - Состояние фар автомобиля.
    
  - `signals` - Состояние сигналов автомобиля.
    
  - `drive_mod` - Передача автомобиля.
    
* ### Создание геттера и сеттера для защищенного атрибута.

  - Значение сеттера `value` ниже проходит `validate_carfuncs_car` перед присваиванием.
    
  - `@property` - Геттер защищенного атрибута `_car` дата-класса CarFuncs.

  - `@car.setter` - Сеттер защищенного атрибута `_car` дата-класса CarFuncs.
    
* ### Валидация атрибутов дата-класса CarFuncs:
  
  - `validate_carfuncs_car` - Ф-ия валидации защищенного атрибута `_car` (Атрибут принадлежит дата-классу Car).
    
  - `validate_carfuncs_enigne` - Ф-ия валидации атрибута `enigne` (Атрибут - bool).
    
  - `validate_carfuncs_lights` - Ф-ия валидации атрибута `lights` (Атрибут - bool).
    
  - `validate_carfuncs_signals` - Ф-ия валидации атрибута `signals` (Атрибут - bool).
    
  - `validate_carfuncs_drive_mod` - Ф-ия валидации атрибута `drive_mod` (Атрибут - bool).
  
* ### Реализация Dunder-методов дата-класса CarFuncs:
  
  - `__str__` - Красивый вывод атрибутов объекта дата-класса Car (`_car`, `enigne` и т.д.)
    
  - `__repr__` - Практически идентичен с `__str__`, разница в формате вывода (Состояние двигателя: `self.engine` - engine = `self.engine`).
    
  - `__eq__` - Метод сравнения двух объектов (Объекты равны при равенстве всех атрибутов (self.engine == other.engine и т.д.)

* ### Бизнес-методы дата-класса CarFuncs:
  
  - `toggle_main_car_funcs_enigne` - Изменение состояния двигателя автомобиля (Вкл/Выкл - T/F).
    
  - `toggle_car_funcs` - Включение/Выключение Сигналов/Фар автомобиля.
    
  - `toggle_drive_mod` - Переключение коробки передач автомобиля (Forward/Reverse/Neutral).

<h1 align = 'center'>demo.py</h1>

> Ниже представлен демонстрационный файл demo.py
> 
> Демонстрация разбита на секции C(3), B(4), A(5).

## Оценка C(3):

* ### Демонстрация инициализации объекта demo_object_01:
![demo_initialization](/misc/images/lab_01/demo/C/demo_initialization.png)
* ### Демонстрация вывода инициализированного объекта demo_object_01 в терминал:
![demo_print](/misc/images/lab_01/demo/C/demo_print.png)

<h3 align = 'center' > ↓ </h3>

![demo_print_terminal](/misc/images/lab_01/demo/C/demo_print_terminal.png)
* ### Демонстрация равенства/неравенства объектов дата-класса Car:
![demo_equalization](/misc/images/lab_01/demo/C/demo_equalization.png)

<h3 align = 'center' > ↓ </h3>

![demo_equalization_terminal](/misc/images/lab_01/demo/C/demo_equalization_terminal.png)
* ### Демонстрация некорректного создания объектов дата-класса Car:
![demo_incorrect_creation](/misc/images/lab_01/demo/C/demo_inocrrect_creation.png)

<h3 align = 'center' > ↓ </h3>

![demo_incorrect_creation_terminal](/misc/images/lab_01/demo/C/demo_incorrect_creation_terminal.png)

## Оценка B(4):
* ### Демонстрация доступа к объекта дата-класса Car через класс/экземпляр:
![demo_access_to_class](/misc/images/lab_01/demo/B/demo_access_to_class.png)

<h3 align = 'center' > ↓ </h3>

![demo_access_to_class_terminal](/misc/images/lab_01/demo/B/demo_access_to_class_terminal.png)
* ### Демонстрация изменения состояния атрибута объекта дата-класса Car:
![demo_property_change_by_setter](/misc/images/lab_01/demo/B/demo_property_change_by_setter.png)

<h3 align = 'center' > ↓ </h3>

![demo_property_change_by_setter_terminal](/misc/images/lab_01/demo/B/demo_property_change_by_setter_terminal.png)


## Оценка A(5):
* ### Демонстрация логических состояних объектов дата-класса Car:
![demo_conditions](/misc/images/lab_01/demo/A/demo_conditions.png)

<h3 align = 'center' > ↓ </h3>

![demo_conditions_terminal](/misc/images/lab_01/demo/A/demo_conditions_terminal.png)
* ### Демонстрация валидации объектов дата-класса Car:
![demo_validation](/misc/images/lab_01/demo/A/demo_validation.png)

<h3 align = 'center' > ↓ </h3>

![demo_validation_terminal](/misc/images/lab_01/demo/A/demo_validation_terminal.png)