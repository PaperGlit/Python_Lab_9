from GlobalVariables import *
from Data.Lab7.BLL.classes.unit_of_work import UnitOfWork
from Data.Lab7.DAL.classes.database_handler import DBHandler
from Data.Lab7.BLL.classes.network_request import NetworkRequest
from rich.console import Console as RichConsole
from rich.table import Table
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

class Console:
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Console, self).__call__(*args, **kwargs)
        else:
            self._instances[self].__init__(*args, **kwargs)
        return self._instances[self]

    def __init__(self):
        self.uow = UnitOfWork(base_api_url)
        self.db_handler = DBHandler()
        self.main()

    def show_history(self):
        history = self.db_handler.fetch_history()
        if not history:
            print("[bold red]No history found![/bold red]")
            return

        headers = ["ID", "Link", "Type", "Entity ID"]
        self.display_table(history, headers, title="Prompt History")

    def export_history(self):
        prompt = input("Choose format to export:\n1 - TXT\n2 - CSV\n3 - JSON\nYour choice: ")
        try:
            match prompt:
                case "1":
                    self.db_handler.export_to_txt()
                    print("History exported to history.txt")
                case "2":
                    self.db_handler.export_to_csv()
                    print("History exported to history.csv")
                case "3":
                    self.db_handler.export_to_json()
                    print("History exported to history.json")
                case _:
                    print("Invalid choice!")
        except Exception as e:
            print(f"An error occurred during export: {e}")

    @staticmethod
    def display_table(data, headers, title="Data Table"):
        console = RichConsole()
        table = Table(title=title, show_header=True, header_style=header_style)
        for header in headers:
            table.add_column(header, justify="center")
        for row in data:
            table.add_row(*[str(cell) for cell in row])
        console.print(table)

    def print_result(self, result):
        prompt_2 = input("1 - Print a table\n"
                         "2 - Print a list\n"
                         "Your choice: ")
        if prompt_2 == "1":
            self.to_table(result)
        elif prompt_2 == "2":
            self.to_list(result)
        else:
            print("Invalid input!")

    def to_table(self, result):
        if not result:
            print("[bold red]No data to display![/bold red]")
            return
        headers = result[0].keys()
        rows = [[str(item.get(header, "")) for header in headers] for item in result]
        self.display_table(rows, headers, title="API Results")

    @staticmethod
    def to_list(result):
        for i in result:
            print()
            for key, value in i.items():
                print(f"{str(key)}: {value}")

    def main(self):
        try:
            while True:
                prompt = input("\n1 - Posts\n2 - Comments\n3 - Albums\n4 - Photos\n5 - Todos\n6 - Users\n"
                               "7 - View History\n8 - Export History\nYour choice: ")
                if prompt == "7":
                    logger.info("[Lab 7] Read prompt history")
                    self.show_history()
                    continue
                elif prompt == "8":
                    logger.info("[Lab 7] Exported prompt history")
                    self.export_history()
                    continue

                entity = entity_map.get(prompt)
                logger.info(f"[Lab 7] Selected entity: {entity}")
                if not entity:
                    break

                action = input("1 - GET\n2 - POST\n3 - PATCH\n4 - DELETE\nYour choice: ")
                match action:
                    case "1":
                        logger.info("[Lab 7] GET request")
                        result = NetworkRequest.get(self.uow, entity, self.db_handler)
                        self.print_result(result)
                    case "2":
                        logger.info("[Lab 7] POST request")
                        NetworkRequest.post(self.uow, entity, self.db_handler)
                    case "3":
                        logger.info("[Lab 7] PATCH request")
                        NetworkRequest.patch(self.uow, entity, self.db_handler)
                    case "4":
                        logger.info("[Lab 7] DELETE request")
                        NetworkRequest.delete(self.uow, entity, self.db_handler)
                    case _:
                        break
        finally:
            self.db_handler.close()