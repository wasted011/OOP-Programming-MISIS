class CarError(Exception):
    """Базовое исключение для ошибок, связанных с автомобилями."""
    pass

class CarNotFoundError(CarError):
    """Вызывается, если автомобиль не найден в коллекции."""
    def __init__(self, car_id: int):
        self.car_id = car_id
        super().__init__(f"Автомобиль с ID {car_id} не найден.")

class DuplicateCarError(CarError):
    """Вызывается при попытке добавить автомобиль с уже существующим ID."""
    def __init__(self, car_id: int):
        self.car_id = car_id
        super().__init__(f"Автомобиль с ID {car_id} уже существует в коллекции.")

class InvalidDataError(CarError):
    """Вызывается при предоставлении некорректных данных об автомобиле."""
    pass
