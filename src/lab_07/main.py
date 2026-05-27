from app import CarApp
from cli import ConsoleInterface

def main() -> None:
    """
    Точка входа в приложение управления гаражом.
    Инициализирует все слои и запускает интерфейс.
    """
    # Путь задается строкой относительно корня lab_07
    storage_path = "Saved/cars.json"
    
    app = CarApp(storage_path=storage_path)
    cli = ConsoleInterface(app)
    cli.run()

if __name__ == "__main__":
    main()