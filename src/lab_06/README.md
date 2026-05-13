<h1 align='center'>container.py</h1>

> В container.py реализована коллекция типизированная коллекция TypedCollection c использованием Generics.

## Импорты:

### Глобальные:

* `datetime` - date (Для работы с датами).

* `typing` - TypeVar, Generic, Protocol, Callable (Для работы с типами).

* `dataclasses` - dataclass, field (Для работы с @dataclass).

### Локальные:

* `validate` - валидация типов, максимального количества элементов, пробега.

### Тайп-вары:

* `T` - тип элементов в коллекции.

* `R` - тип результата после применения метода map().

* `M` - тип элементов, поддерживающих маппинг (с баундом Mapable).

* `S` - тип элементов, поддерживающих сортировку (с баундом Sortable).

### Протоколы:

* `Mapable` - протокол для элементов, поддерживающих маппинг (Если класс имеет метод map_by - косвенно связан с Mapable).

* `Sortable` - протокол для элементов, поддерживающих сортировку (Если класс имеет метод sort_by - косвенно связан с Sortable).

### Типизированная коллекция (TypedCollection(Generic[T])):

#### Атрибуты:

* `_items` - Закрытый атрибут TypedCollection (Контейнер объектов; type: list[T])

* `_max_items` - Закрытый атрибут TypedCollection (Максимальное количество элементов; type: int)

#### Инкапсуляция:

- #### Геттеры:

    * `items` - Свойство для доступа к элементам коллекции (type: list[T])

    * `max_items` - Свойство для доступа к максимальному количеству элементов (type: int)

- #### Сеттеры:

    * `max_items` - Сеттер для установки максимального количества элементов (type: int)

#### Методы:

- #### Дандер-методы:

    * `__len__` - Получение длины коллекции (type: int)

    * `__str__` - Получение строкового представления коллекции (type: str)

    * `__repr__` - Получение строкового представления коллекции (type: str)

- #### Основные методы:

    * `add` - Добавление элемента в коллекцию (type: T).

    * `remove` - Удаление элемента из коллекции (type: T).

    * `get_all` - Получение всех элементов коллекции (type: list[T]).

    * `find_by_mileage` - Поиск элемента по пробегу (type: T | None).

    * `remove_at` - Удаление элемента по индексу (type: None).
    
    * `get_most_used` - Получение самых используемых элементов (type: list[T]).
    
    * `get_oldest` - Получение самых старых элементов (type: list[T]).
    
    * `get_vehicle_by_type` - Получение элементов по типу (type: list[T]).
    
    * `sort_by` - Сортировка элементов по функции-стратегии (type: None).
    
    * `filter_by` - Фильтрация элементов по функции-стратегии (type: list[T]).
    
    * `apply` - Применение операции (функции-стратегии) к элементам (type: None).
    
    * `find_by` - Поиск элемента по предикату (функции-стратегии) (type: T | None).
    
    * `map_by` - Маппинг элементов (функции-стратегии) (type: list[R]).

<h1 align='center'>validate.py</h1>

> Ниже приведен перечень функций используемых для валидации атрибутов/параметров классов и функций.

* `validate_max_items` - Валидация максимального количества элементов (type: None)

* `validate_generic_type` - Валидация типа элементов (type: None)

* `validate_mileage` - Валидация пробега (type: None)

* `validate_index` - Валидация индекса (type: None)

* `validate_callable` - Валидация функции-стратегии (type: None)

<h1 align='center'>demo.py</h1>

> В demo.py реализована демонстрация работы TypedCollection.
>
> Разбит на три части: `for_three()`, `for_four()` и `for_five()`.

## Локальные импорты:

* `containter` - Импорт TypedCollection.

* `validate` - Импорт валидационных функций.

* `base` - Импорт базового класса Car.

## `for_three()`:

![for_three_code](/misc/images/lab_06/for_three/three_code.png)

<p align="center"> ↓ </p>

![for_three_terminal](/misc/images/lab_06/for_three/three_terminal.png)

## `for_four()`:

![for_four_code](/misc/images/lab_06/for_four/four_code.png)

<p align="center"> ↓ </p>

![for_four_terminal](/misc/images/lab_06/for_four/four_terminal.png)

## `for_five()`:

![for_five_code](/misc/images/lab_06/for_five/five_code.png)

<p align="center"> ↓ </p>

![for_five_terminal](/misc/images/lab_06/for_five/five_terminal.png)
