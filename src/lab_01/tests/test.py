import pytest
from datetime import date
from src.lab_01.main.model import Car, CarFuncs
from src.lab_01.main.validate import *

equation_test = [
    
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "Toyota", "Camry", 50000, date(2015, 1, 1)),
    ("Honda", "Civic", 30000, date(2018, 1, 1), "Mazda", "Miata", 20000, date(2017, 1, 1))

]

incorrect_creation_test = [

    (" ", "Camry", 50000, date(2015, 1, 1), ValueError),
    ("Toyota", " ", 50000, date(2015, 1, 1), ValueError)

]

change_setter_test = [

    ("Toyota", "Camry", 50000, date(2015, 1, 1), "mileage", 60000, None),
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "year_of_manufacture", date(2024, 1, 1), None)

]

restriction_setter_test = [

    ("Toyota", "Camry", 50000, date(2015, 1, 1), "mileage", -100, ValueError),
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "year_of_manufacture", date(2028, 1, 1), ValueError)

]

access_to_attribute_test = [

    ("Toyota", "Camry", 50000, date(2015, 1, 1), "brand", "Toyota"),
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "model", "Camry")

]

validation_test = [
    
    ("Toyota", "brand", True),
    ("", "model", False)

]

conditions_test = [

    (Car(_brand="Toyota",_model="Camry", _mileage=50000, _year_of_manufacture=date(2015, 1, 1)), True, True, True, "Neutral", "lights", False),
    (Car(_brand="Toyota",_model="Camry", _mileage=50000, _year_of_manufacture=date(2015, 1, 1)), False, False, False, "Neutral", "signals", False)

]

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, brand2, model2, mileage2, year_of_manufacture2', equation_test)
def test_eq(brand, model, mileage, year_of_manufacture, brand2, model2, mileage2, year_of_manufacture2):
    test_class_object_01 = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    test_class_object_02 = Car(_brand=brand2, _model=model2, _mileage=mileage2, _year_of_manufacture=year_of_manufacture2)
    
    if brand == brand2:
        assert test_class_object_01 == test_class_object_02
    else:
        assert test_class_object_01 != test_class_object_02

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, expected', incorrect_creation_test)
def test_incorrect_creation(brand, model, mileage, year_of_manufacture, expected):
    with pytest.raises(expected):
        Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, attribute, value, expected', change_setter_test)
def test_change_setter(brand, model, mileage, year_of_manufacture, attribute, value, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    assert setattr(source, attribute, value) == expected

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, attribute, value, expected', restriction_setter_test)
def test_restriction_setter(brand, model, mileage, year_of_manufacture, attribute, value, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    with pytest.raises(expected):
        setattr(source, attribute, value)
    
@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, attribute, expected', access_to_attribute_test)
def test_access_to_atribute(brand, model, mileage, year_of_manufacture, attribute, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    assert getattr(source, attribute) == expected

@pytest.mark.parametrize('element, attribute, expected', validation_test)
def test_validation(element, attribute, expected):
    if attribute == "brand":
        source = validate_car_brand(element)
    elif attribute == "model":
        source = validate_car_model(element)
    elif attribute == "mileage":
        source = validate_mileage(element)
    elif attribute == "year_of_manufacture":
        source = validate_year_of_manufacture(element)
        
    assert source == expected

@pytest.mark.parametrize('car_object, engine_status, lights_status, signals_status, drive_mod, func, expected', conditions_test)
def test_conditions(car_object, engine_status, lights_status, signals_status, drive_mod, func, expected):
    source = CarFuncs(car_object, engine=engine_status, lights=lights_status, signals=signals_status, drive_mod=drive_mod)

    if func in ['lights', 'signals']:
        source.toggle_car_funcs(func)

    else:
        raise ValueError

    assert getattr(source, func) == expected