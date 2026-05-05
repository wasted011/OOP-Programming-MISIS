<h1 align = 'center'>strategies.py</h1>

> В strategies.py реализованы функции/стратегии/алгоритмы/ методы для работы с коллекцией автомобилей

## Импорты:

### Глобальные импорты:

* `typing` - Импорт `TypeVar` и `Callable`
* `datetime` - Импорт `date`

### Локальные импорты:

* `.validate` - Импорт `validate_mileage`

##  Ф-ии для применения map() метода:

* `add_mileage` - Добавление 10000 к пробегу автомобиля.

## Фабрика функций:

* `filter_by_mileage_fabric` - Фабрика функций для фильтрации автомобилей по пробегу.

## Ф-ии для сортировки объектов методом .sort_by():

* `sort_by_brand` - Сортировка автомобилей по бренду.

* `sort_by_model` - Сортировка автомобилей по модели.

* `sort_by_mileage` - Сортировка автомобилей по пробегу.

* `sort_by_year_of_manufacture` - Сортировка автомобилей по году выпуска.

## Ф-ии для фильтрации объектов методом .filter_by():

* `filter_by_brand` - Фильтрация автомобилей по бренду (например, "Toyota").

* `filter_by_model` - Фильтрация автомобилей по модели (например, "Camry").

* `filter_by_mileage` - Фильтрация автомобилей по пробегу (например, <= 50000).

* `filter_by_year_of_manufacture` - Фильтрация автомобилей по году выпуска (например, >= 2020).

## Ф-ии для применения apply() метода:

* `apply_mileage_increase` - Увеличение пробега автомобиля на 10000.

* `apply_mileage_decrease` - Уменьшение пробега автомобиля на 10000.

# Callable-объекты (стратегии):

* `IncreaseMileageStrategy` - Увеличение пробега автомобиля на 50%.

* `DecreaseMileageStrategy` - Уменьшение пробега автомобиля на 50%.

<h1 align = 'center'>demo.py</h1>

> В demo.py реализованы функции для демонстрации работы с коллекцией автомобилей.

### Локальные импорты:

* `.strategies` - Импорт всех функций из strategies.py

* `.collection` - Импорт класса Collection из collection.py

* ## `for_three()`:

![for_three_code](/misc/images/lab_05/for_three/three_code.png)

<p align="center"> ↓ </p>

![for_three_terminal](/misc/images/lab_05/for_three/three_temrinal.png)

* ## `for_four()`:

![for_four_code](/misc/images/lab_05/for_four/four_code.png)

<p align="center"> ↓ </p>

![for_four_terminal](/misc/images/lab_05/for_four/four_terminal.png)

* ## `for_five()`:

![for_five_code](/misc/images/lab_05/for_five/five_code.png)

<p align="center"> ↓ </p>

![for_five_terminal](/misc/images/lab_05/for_five/five_terminal.png)