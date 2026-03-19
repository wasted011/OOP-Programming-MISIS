from model import Car, CarFuncs
from validate import validate_mileage

from datetime import date
from dataclasses import dataclass

# Инициализация(создание) объекта класса Car.
"""
demo_object_01 = Car(
    _brand="Toyota",
    _model="Camry",
    _mileage=50000,
    _year_of_manufacture=date(2015, 1, 1),
)

print("Вывод инициализированного объекта demo_object через print() (__repr__, __str__): ")
print(demo_object_01.__str__())
print(demo_object_01.__repr__())


# Сравнение двух объектов (demo_object_02, demo_object_03) (Dunder-метод: __eq__).

demo_object_02 = Car(
    _brand="Honda",
    _model="Civic",
    _mileage=45000,
    _year_of_manufacture=date(2000, 1, 1),
)
demo_object_03 = Car(
    _brand="Masserati",
    _model="Quattroporte",
    _mileage=50000,
    _year_of_manufacture=date(2025, 1, 1),
)

# test_demo_object_02 - Для того, чтобы показать что если объекты имеют идентичные атрибуты, они равны.

test_demo_object_02 = Car(
    _brand="Honda",
    _model="Civic",
    _mileage=45000,
    _year_of_manufacture=date(2000, 1, 1),
)

def demo_equalization(variable_01: Car, variable_02: Car) -> bool:

    return variable_01 == variable_02


print(f"Первый объект: {demo_object_02}")
print(f"Второй объект: {demo_object_03}")

print("Случай неравенства объектов:")
print(demo_equalization(variable_01=demo_object_02, variable_02=demo_object_03))

print("Случай равенства объектов:")
print(demo_equalization(variable_01=demo_object_02, variable_02=test_demo_object_02))
"""
"""
# Примеры некорректного создания.

demo_object_04 = ("", "Camry", 50000, date(2015, 1, 1))
demo_object_05 = ("Toyota", "", 50000, date(2015, 1, 1))


def demo_incorrect_initialization(variable: tuple) -> None | str:

    try:

        Car(
            _brand=variable[0],
            _model=variable[1],
            _mileage=variable[2],
            _year_of_manufacture=variable[3],
        )

    except ValueError as error:

        return f"Inocorrect initialization, Error: {error}"
print(f"Первый объект: {demo_object_04}")
print("Для объекта demo_object_04 поднимет ValueError:")
print(demo_incorrect_initialization(variable=demo_object_04))

print(f"Второй объект: {demo_object_05}")
print("Для объекта demo_object_05 аналогично demo_object_04 поднимет ValueError:")
print(demo_incorrect_initialization(variable=demo_object_05))
"""
"""
# Пример изменения свойства объекта через setter.

demo_object_06 = Car(
    _brand="Toyota",
    _model="Camry",
    _mileage=50000,
    _year_of_manufacture=date(2015, 1, 1),
)


def demo_change_setter(variable: Car, new_mileage: int) -> str:

    if not validate_mileage(new_mileage):
        raise ValueError("Incorrect new_mileage value")

    try:
        variable.mileage = new_mileage
        return "Succesfully"

    except ValueError:
        return "Not succesfully"

print("Присвоит значение 50000:")
print(demo_change_setter(variable=demo_object_06, new_mileage=50000))

print("Поднимет ValueError: Новое значение не прошло валидацию в @mileage.setter")
print(demo_change_setter(variable=demo_object_06, new_mileage=-50000))

"""


# Пример доступа к атрибуту класса через класс и экземпляр.

# Доступ через класс:

# (т. к. В аттрибутах класса Car нет какого-то определенного (все атрибуты задаются пользователем), создам класс CarWithOnlyDoors с уже определенным атрибутом doors чтобы показать доступ через класс)

"""
@dataclass
class CarWithOnlyDoors:

    doors: int = 4

print("Доступ через класс:")
print(CarWithOnlyDoors.doors)

demo_examplar = Car(
    _brand="Ford",
    _model="Mustang",
    _mileage=10000,
    _year_of_manufacture=date(2018, 1, 1),
)

print("Доступ через экземпляр:")
print(demo_examplar.mileage)
"""


"""
# Демонастрация валидации.

scenario_01 = ("Porshe", "", 30000, date(2022, 1, 1))
scenario_02 = ("", "GT3-RS", 45000, date(2023, 1, 1))
scenario_03 = ("Porshe", "GT3-RS", -35000, date(2024, 1, 1))
success_scenario = ("Porshe", "GT3-RS", 35000, date(2025, 1, 1))


def demo_validation(variable: tuple) -> None | str:

    try:

        Car(
            _brand=variable[0],
            _model=variable[1],
            _mileage=variable[2],
            _year_of_manufacture=variable[3],
        )
        return "All elements succesfully passed the validation proccess"

    except ValueError as error:
        return f"An error occured: {error}"

print("Поднимет ValueError: Второй атрибут не прошел валидацию в @model.setter")
print(demo_validation(variable=scenario_01))
print("Поднимет ValueError: Первый атрибут не прошел валидацию в @brand.setter")
print(demo_validation(variable=scenario_02))

print("Поднимет ValueError: Третий атрибут не прошел валидацию в @mileage.setter")
print(demo_validation(variable=scenario_03))
print("Вернет: All elements succesfully passed the validation proccess")
print(demo_validation(variable=success_scenario))
"""

# Демонстрация лог. состояний.

scenario_04 = Car(
    _brand="Porshe",
    _model="Panamera",
    _mileage=10000,
    _year_of_manufacture=date(2024, 1, 1),
)
scenario_05 = Car(
    _brand="Pagani Zonda",
    _model="R",
    _mileage=5000,
    _year_of_manufacture=date(2010, 1, 1),
)
scenario_06 = Car(
    _brand="Audi", 
    _model="R8", 
    _mileage=25000, 
    _year_of_manufacture=date(2015, 1, 1)
)

final_scenario_04 = CarFuncs(scenario_04, True, False, False, "Neutral")
final_scenraio_05 = CarFuncs(scenario_05, False, False, False, "Neutral")
final_scenraio_06 = CarFuncs(scenario_06, True, True, True, "Forward")


def demo_log_properties(variable: CarFuncs, func: str):

    if not isinstance(variable, CarFuncs):
        raise ValueError

    if not isinstance(func, str) or func not in ["lights", "signals", "drive_mod"]:
        return "Incorrect function"

    try:

        if variable.engine:

            if func in ["lights", "signals"]:
                variable.toggle_car_funcs(func)

                return f"Succesfully changed {func}."

            elif func == "drive_mod":

                which_func = input("Choose an option: Forward, Backward, Neutral: ")

                if which_func in ["Forward", "Backward", "Neutral"]:
                    variable.toggle_drive_mod(which_func)
                    return f"Succesfully changed {func}."

                return "Incorrect option"
        else:
            raise ValueError("Engine is Off")

    except ValueError as error:
        return f"An error has occured: {error}"

print("Сценарий 1: Выведет 'Succesfully changed 'lights'.")
print(demo_log_properties(variable=final_scenario_04, func="lights"))

print("Сценарий 2: Поднимет ValueError. Выведет 'An error has occured: Engine is off")
print(demo_log_properties(variable=final_scenraio_05, func="signals"))

print("Сценарий 3: Попросит выбрать передачу, после выбора выведет 'Succesfully changed drive_mod'.")
print(demo_log_properties(variable=final_scenraio_06, func="drive_mod"))