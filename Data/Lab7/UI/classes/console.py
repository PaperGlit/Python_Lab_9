"""The user interface of the lab work"""
import requests
from rich.console import Console as RichConsole
from rich.table import Table
import global_variables
from Data.Lab7.BLL.classes.unit_of_work import UnitOfWork
from Data.Lab7.DAL.classes.database_handler import DBHandler
from Data.Lab7.BLL.classes.network_request import NetworkRequest
from Data.Shared.classes.singleton import Singleton
from Data.Shared.classes.unit_test import UnitTest
from Data.Shared.functions.logger import logger


class Console(Singleton):
    """The console class of this lab work"""
    def __init__(self):
        self.uow = UnitOfWork(global_variables.BASE_API_URL)
        self.db_handler = DBHandler()
        self.main()

    def show_history(self):
        """Shows the user their history"""
        history = self.db_handler.fetch_history()
        if not history:
            print("[bold red]No history found![/bold red]")
            return

        headers = ["ID", "Link", "Type", "Entity ID"]
        self.display_table(history, headers, title="Prompt History")

    def export_history(self):
        """Exports history database to a file"""
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
        except IOError as e:
            print(f"An error occurred during export: {e}")

    @staticmethod
    def display_table(data, headers, title="Data Table"):
        """Displays a response table"""
        console = RichConsole()
        table = Table(title=title, show_header=True, header_style=global_variables.HEADER_STYLE)
        for header in headers:
            table.add_column(header, justify="center")
        for row in data:
            table.add_row(*[str(cell) for cell in row])
        console.print(table)

    def print_result(self, result):
        """Prints a response into a console interface"""
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
        """Transforms a response into a table"""
        if not result:
            print("[bold red]No data to display![/bold red]")
            return
        headers = result[0].keys()
        rows = [[str(item.get(header, "")) for header in headers] for item in result]
        self.display_table(rows, headers, title="API Results")

    @staticmethod
    def to_list(result):
        """Transform a response into a list"""
        for i in result:
            print()
            for key, value in i.items():
                print(f"{str(key)}: {value}")

    def main(self):
        """The main menu of this lab work"""
        try:
            while True:
                prompt = input("\n1 - Posts\n2 - Comments\n3 - Albums\n"
                               "4 - Photos\n5 - Todos\n6 - Users\n"
                               "7 - View History\n8 - Export History\n9 - Unit tests\nYour choice: ")
                if prompt == "7":
                    logger.info("[Lab 7] Read prompt history")
                    self.show_history()
                    continue
                if prompt == "8":
                    logger.info("[Lab 7] Exported prompt history")
                    self.export_history()
                    continue
                if prompt == "9":
                    logger.info("[Lab 7] Started unit tests")
                    UnitTest.run_unit_tests()
                    continue

                entity = global_variables.ENTITY_MAP.get(prompt)
                logger.info("[Lab 7] Selected entity: %s", entity)
                if not entity:
                    break

                action = input("1 - GET\n2 - POST\n3 - PATCH\n4 - DELETE\nYour choice: ")
                match action:
                    case "1":
                        logger.info("[Lab 7] GET request")
                        try:
                            result = NetworkRequest.get(self.uow, entity, self.db_handler)
                            self.print_result(result)
                        except requests.HTTPError as e:
                            logger.warning(e)
                            print(e)
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
