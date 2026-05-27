from datetime import date
from typing import Optional, Any, Callable
from app import CarApp
from models import Car, ElectricCar, SportCar
from exceptions import CarError, CarNotFoundError, DuplicateCarError

class ConsoleInterface:
    """
    Консольный интерфейс приложения.
    Обеспечивает взаимодействие с пользователем и управление гаражом.
    """

    def __init__(self, app: CarApp):
        """
        Инициализирует интерфейс.
        
        :param app: Экземпляр приложения (бизнес-логика).
        """
        self._app = app
        # Диспетчер команд главного меню
        self._actions: dict[str, Callable[[], None]] = {
            "1": self._display_cars,
            "2": self._add_car_dialog,
            "3": self._delete_car_dialog,
            "4": self._search_dialog,
            "5": self._filter_dialog,
            "6": self._sort_dialog
        }
        # Диспетчер создания типов автомобилей
        self._creators: dict[str, Callable[[dict[str, Any]], Car]] = {
            "1": self._create_standard,
            "2": self._create_electric,
            "3": self._create_sport
        }

    def _get_input(self, prompt: str) -> str:
        """Вспомогательный метод для получения ввода."""
        return input(prompt).strip()

    def _display_cars(self, cars: Optional[list[Car]] = None) -> None:
        """Выводит список автомобилей в консоль."""
        target_list = cars if cars is not None else self._app.get_all_cars()
        
        if not target_list:
            print("\nИнформационное сообщение: База данных пуста.")
            return

        print("\n--- Список зарегистрированных автомобилей ---")
        for car in target_list:
            print(f"Запись: {car}")
        print("---------------------------------------------")

    def _create_standard(self, args: dict[str, Any]) -> Car:
        """Создает стандартный автомобиль."""
        return Car(**args)

    def _create_electric(self, args: dict[str, Any]) -> ElectricCar:
        """Создает электромобиль с дополнительными параметрами."""
        cap = int(self._get_input("Введите емкость аккумулятора (кВт*ч): "))
        level = int(self._get_input("Введите текущий уровень заряда (%): "))
        return ElectricCar(**args, battery_capacity=cap, charge_level=level)

    def _create_sport(self, args: dict[str, Any]) -> SportCar:
        """Создает спорткар с дополнительными параметрами."""
        speed = int(self._get_input("Введите максимальную скорость (км/ч): "))
        acc = float(self._get_input("Введите время разгона 0-100 (сек): "))
        return SportCar(**args, max_speed=speed, acceleration=acc)

    def _add_car_dialog(self) -> None:
        """Диалог добавления нового транспортного средства."""
        print("\nТипы транспорта:\n1. Стандартный автомобиль\n2. Электромобиль\n3. Спортивный автомобиль")
        choice = self._get_input("Выберите тип для добавления: ")
        
        creator = self._creators.get(choice)
        if not creator:
            print("Ошибка: Выбран неизвестный тип транспорта.")
            return

        try:
            car_id = int(self._get_input("Введите уникальный ID: "))
            brand = self._get_input("Введите марку производителя: ")
            model = self._get_input("Введите название модели: ")
            mileage = int(self._get_input("Введите текущий пробег: "))
            year = int(self._get_input("Введите год производства: "))

            common_args = {
                "id": car_id,
                "brand": brand,
                "model": model,
                "mileage": mileage,
                "year_of_manufacture": date(year, 1, 1)
            }

            car = creator(common_args)
            self._app.add_car(car)
            print("Результат: Транспортное средство успешно добавлено в базу.")

        except (ValueError, CarError) as e:
            print(f"Ошибка при сохранении: {e}")

    def _delete_car_dialog(self) -> None:
        """Удаление записи из базы с подтверждением."""
        try:
            car_id = int(self._get_input("Введите ID записи для удаления: "))
            car = self._app.find_car_by_id(car_id)
            
            confirm = self._get_input(f"Вы действительно хотите удалить {car}? (y/n): ")
            if confirm.lower() == 'y':
                self._app.delete_car(car_id)
                print("Результат: Запись успешно удалена.")
            else:
                print("Информационное сообщение: Операция отменена.")
        except (ValueError, CarError) as e:
            print(f"Ошибка удаления: {e}")

    def _search_dialog(self) -> None:
        """Поиск автомобиля по марке или модели."""
        print("\nПараметры поиска:\n1. Поиск по марке\n2. Поиск по модели")
        choice = self._get_input("Выберите поле для поиска: ")
        
        if choice == "1":
            brand = self._get_input("Введите марку для поиска: ")
            results = self._app.filter_cars(lambda c: c.brand.lower() == brand.lower())
            self._display_cars(results)
        elif choice == "2":
            model = self._get_input("Введите модель для поиска: ")
            results = self._app.filter_cars(lambda c: c.model.lower() == model.lower())
            self._display_cars(results)
        else:
            print("Ошибка: Некорректный выбор параметра поиска.")

    def _filter_dialog(self) -> None:
        """Фильтрация коллекции по техническим критериям."""
        print("\nКритерии фильтрации:\n1. Пробег выше заданного\n2. Только электромобили")
        choice = self._get_input("Выберите критерий: ")

        if choice == "1":
            try:
                limit = int(self._get_input("Введите минимальный пробег: "))
                results = self._app.filter_cars(lambda c: c.mileage > limit)
                self._display_cars(results)
            except ValueError:
                print("Ошибка: Введено некорректное числовое значение.")
        elif choice == "2":
            results = self._app.filter_cars(lambda c: isinstance(c, ElectricCar))
            self._display_cars(results)
        else:
            print("Ошибка: Некорректный выбор критерия.")

    def _sort_dialog(self) -> None:
        """Сортировка базы данных по выбранному полю."""
        print("\nПоля для сортировки:\n1. Идентификатор\n2. Марка\n3. Пробег\n4. Год выпуска")
        choice = self._get_input("Выберите поле: ")
        reverse = self._get_input("Использовать обратный порядок? (y/n): ").lower() == 'y'

        strategy_map = {
            "1": lambda c: c.id,
            "2": lambda c: c.brand.lower(),
            "3": lambda c: c.mileage,
            "4": lambda c: c.year_of_manufacture
        }

        if choice in strategy_map:
            self._app.sort_cars(strategy_map[choice], reverse=reverse)
            print("Результат: Сортировка успешно выполнена.")
            self._display_cars()
        else:
            print("Ошибка: Выбрано несуществующее поле для сортировки.")

    def run(self) -> None:
        """Запускает основной цикл обработки пользовательских команд."""
        while True:
            print("\n--- ГЛАВНОЕ МЕНЮ УПРАВЛЕНИЯ ГАРАЖОМ ---")
            print("1. Вывести список всех автомобилей")
            print("2. Добавить новую машину в базу")
            print("3. Удалить машину из базы по ID")
            print("4. Найти машину по параметрам")
            print("5. Фильтровать список машин")
            print("6. Отсортировать базу данных")
            print("0. Сохранить изменения и завершить работу")
            print("---------------------------------------")
            
            choice = self._get_input("Выберите пункт меню: ")

            if choice == "0":
                self._app.save_data()
                print("Информационное сообщение: Данные успешно сохранены. Завершение работы...")
                break
            
            action = self._actions.get(choice)
            if action:
                try:
                    action()
                except Exception as e:
                    print(f"Критическая ошибка: {e}")
            else:
                print("Ошибка: Выбран несуществующий пункт меню.")