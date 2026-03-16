<h1 align = 'center' >model.py</h1>

---
> В model.py реализованно 2 дата-класса (Car и CarFuncs):
> 
> Car: Инициализирует всю первичную информацию о автомобиле (Прозводитель, модель и т. д.).
> 
> CarFuncs: Основные функции автомобиля (Вкл/Выкл фар/сигналов и т. д.).
>
> Ниже представлены скриншоты частей кода, действия описаны комментариями в коде/в заголовках перед скриншотами.
---

## Дата-класс Car:

* ### Инициализация дата-класса Car и его атрибутов:
![](/misc/images/lab_01/model/Class_Car/car_data_class_initialization.png)
* ### Валидация атрибутов дата-класса Car:
![](/misc/images/lab_01/model/Class_Car/car_validation.png)
* ### Создание геттеров для защищенных атрибутов (_variable) дата-класса Car:
![](/misc/images/lab_01/model/Class_Car/car_getters.png)
* ### Создание сеттеров для защищенных атрибутов дата-класса Car:
![](/misc/images/lab_01/model/Class_Car/car_setters.png)
* ### Реализация Dunder-методов дата-класса Car:
![](/misc/images/lab_01/model/Class_Car/car_dunder_methods.png)

## Дата-класс CarFuncs:

* ### Инициализация дата-класса CarFuncs и его атрибутов:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_data_class_initialization.png)
* ### Создание геттера для защищенного атрибута car дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_getter.png)
* ### Создание сеттера для защищенного атрибута car дата-класса Carfuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_setter.png)
* ### Валидация атрибутов дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_validation.png)
* ### Реализация Dunder-методов дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_dunder_methods.png)
* ### Метода запуска мотора автомобиля объекта дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_toggle_engine_method.png)
* ### Метод Вкл/Выкл Фар/Сигналов объекта дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_toggle_lights_signals.png)
* ### Метод переключения коробки передач объекта дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_toggle_drive_mod_method.png)
* ### Метод имитации движения (+Пробег) автомобиля объекта дата-класса CarFuncs:
![](/misc/images/lab_01/model/Class_CarFuncs/carfuncs_drive_method.png)

<h1 align = 'center'>validate.py</h1>

---
> Ниже представлены функции валидации конкретных переменных/атрибутов
> используемых в model.py
---

* ## Ф-ия валидации защищенного атрибута brand:
![](/misc/images/lab_01/validate/validate_car_brand.png)
* ## Ф-ия валидации защищенного атрибута model:
![](/misc/images/lab_01/validate/validate_car_model.png) 
* ## Ф-ия валидации защищенного атрибута mileage:
![](/misc/images/lab_01/validate/validate_mileage.png)
* ## Ф-ия валидации защищенного атрибута year_of_manufacture:
![](/misc/images/lab_01/validate/validate_year_of_manufacture.png)
* ## Валидация защищенного атрибута car дата-класса CarFuncs (Прописана в __post_init__):
![](/misc/images/lab_01/validate/validate_type_car.png)
* # Валидация атрибутов lights/signals дата-класса СarFuncs:
![](/misc/images/lab_01/validate/validate_lights_signals.png)
* ## Ф-ия валидации передач атритуба drive_mod:
![](/misc/images/lab_01/validate/validate_drive_mod.png)
* ## Ф-ия валидации переменной distance метода drive дата-класса CarFuncs:
![](/misc/images/lab_01/validate/validate_distance.png)

<h1 align = 'center'>demo.py</h1>

---
> Ниже представлен демонстрационный файл demo.py
> Демонстрация разбита на секции C(3), B(4), A(5).
---

## Оценка C(3):

* ### Демонстрация инициализации объекта demo_object_01:
![](/misc/images/lab_01/demo/C/demo_initialization.png)
* ### Демонстрация вывода инициализированного объекта demo_object_01 в терминал:
![](/misc/images/lab_01/demo/C/demo_print.png)
* ### Демонстрация равенства/неравенства объектов дата-класса Car:
![](/misc/images/lab_01/demo/C/demo_equalization.png)
* ### Демонстрация некорректного создания объектов дата-класса Car:
![](/misc/images/lab_01/demo/C/demo_inocrrect_creation.png)

## Оценка B(4):
* ### Демонстрация доступа к объекта дата-класса Car через класс/экземпляр:
![](/misc/images/lab_01/demo/B/demo_access_to_class.png)
* ### Демонастрация изменения состояния атрибута объекта дата-класса Car:
![](/misc/images/lab_01/demo/B/demo_access_to_class.png)

## Оценка A(5):
* ### Демонстрация логических состояних объектов дата-класса Car:
![](/misc/images/lab_01/demo/A/demo_conditions.png)
* ### Демонстрация валидации объектов дата-класса Car:
![](/misc/images/lab_01/demo/A/demo_validation.png)
