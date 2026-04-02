from src.lab_01.main.model import Car
from src.lab_02.main.validate import (
    validate_car_id
)

from dataclasses import dataclass, field
from datetime import date
@dataclass
class Garage:

    _cars: dict[int, dict] = field(default_factory=dict)
    _last_id: int = 0

    @property
    def cars(self): return self._cars

    @property
    def last_id(self): return self._last_id

    def add_car(self, new_object: Car):

        if not isinstance(new_object, Car):
            raise TypeError
        
        current_id = self._last_id
        self._last_id += 1
        
        new_car = {
            "Brand": new_object.brand,
            "Model": new_object.model,
            "Mileage": new_object.mileage,
            "Year_of_manufacture": new_object.year_of_manufacture
        }
        if new_car not in self._cars.values():

            self._cars.update({current_id:new_car})
            return "Succesfully added"
        
        return "Car is already in garage"
        
    def find_by_id(self, car_id: int):

        if validate_car_id(car_id):

            if car_id in self._cars:

                return self._cars[car_id]
            
            return "No car with that id"

    def delete_car(self, car_id: int):

        if validate_car_id(car_id):

            if car_id in self._cars:

                del self._cars[car_id]
                return "Succesfully deleted"
            
            return "No car with that id"
    
    def get_all(self):
        print("-----")
        for car_id in self._cars:
            for key in self._cars[car_id]:
                if key != "Year_of_manufacture":
                    print(f"{key}: {self._cars[car_id][key]}; ", end = '')
                print(f"{key}: {self._cars[car_id][key]}.", end = '')
            print('')
        return "-----"
    
    def update_car_info(self, car_id: int, key: str, updated_value: any):

        if validate_car_id(car_id):
        
            if not isinstance(key, str):
                raise TypeError
            
            if not updated_value or updated_value == '':
                raise ValueError

            if car_id not in self._cars:
                raise ValueError
            
            if key not in self._cars[car_id]:
                raise ValueError
        
            self._cars[car_id][key] = updated_value
            return "Succesfully updated"
        
#smth