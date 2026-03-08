import sys, datetime
sys.path.append('2nd sem/src/lab_01/main')

from datetime import date
from src.lab_01.main.model import Car, CarFuncs
import pytest

equation_test = [
    
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "Toyota", "Camry", 50000, date(2015, 1, 1)),
    ("Honda", "Civic", 30000, date(2018, 1, 1), "Mazda", "Miata", 20000, date(2017, 1, 1))

]

incorrect_creation_test = [

    ("", "Camry", 50000, date(2015, 1, 1), "Invalid brand value."),
    ("Toyota", "", 50000, date(2015, 1, 1), "Invalid model value.")

]

change_setter_test = [

    ("Toyota", "Camry", 50000, date(2015, 1, 1), "mileage", 60000, None),
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "year_of_manufacture", date(2024, 1, 1), None)

]

restriction_setter_test = [

    ("Toyota", "Camry", 50000, date(2015, 1, 1), "mileage", -100, "Invalid mileage value."),
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "year_of_manufacture", date(2028, 1, 1), "Invalid year of manufacture value.")

]

access_to_attribute_test = [

    ("Toyota", "Camry", 50000, date(2015, 1, 1), "brand", "Toyota")
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "model", "Camry")

]

validation_test = [
    
    ("Toyota", "Camry", 50000, date(2015, 1, 1), "brand", True)
    ("", "Camry", 50000, date(2015, 1, 1), "brand", False)

]

conditions_test = [

    (Car(_brand="Toyota",_model="Camry", _mileage=50000, _year_of_manufacture=date(2015, 1, 1)), True, True, True, "Neutral", "Lights turned Off.")
    (Car(_brand="Toyota",_model="Camry", _mileage=50000, _year_of_manufacture=date(2015, 1, 1)), False, False, False, "Forward", "Cannot change drive mode. The engine is off.")

]

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, brand2, model2, mileage2, year_of_manufacture2', equation_test)
def test_eq(brand, model, mileage, year_of_manufacture, brand2, model2, mileage2, year_of_manufacture2):
    test_class_object_01 = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    test_class_object_02 = Car(_brand=brand2, _model=model2, _mileage=mileage2, _year_of_manufacture=year_of_manufacture2)
    assert test_class_object_01 == test_class_object_02

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, expected', incorrect_creation_test)
def test_incorrect_creation(brand, model, mileage, year_of_manufacture, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    assert source == expected

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, attribute, value, expected', change_setter_test)
def test_change_setter(brand, model, mileage, year_of_manufacture, attribute, value, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    assert setattr(source, attribute, value) == expected

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, attribute, value, expected', restriction_setter_test)
def test_restriction_setter(brand, model, mileage, year_of_manufacture, attribute, value, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    assert setattr(source, attribute, value) == expected
    
@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture, attribute, expected', access_to_attribute_test)
def test_access_to_atribute(brand, model, mileage, year_of_manufacture, attribute, expected):
    source = Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture)
    assert getattr(source, attribute) == expected

@pytest.mark.parametrize('brand, model, mileage, year_of_manufacture attribute expected', validation_test)
def test_validation(brand, model, mileage, year_of_manufacture, attribute, expected):
    source = getattr(Car(_brand=brand, _model=model, _mileage=mileage, _year_of_manufacture=year_of_manufacture), attribute)
    assert source == expected

@pytest.mark.parametrize('object, engine_status, lights_status, signals_status, drive_mod, expected', conditions_test)
def test_conditions(object, engine_status, lights_status, signals_status, drive_mod, expected):
    source = CarFuncs(object, engine=engine_status, lights=lights_status, signals=signals_status, drive_mod=drive_mod).toggle_car_funcs('lights')
    assert source == expected
