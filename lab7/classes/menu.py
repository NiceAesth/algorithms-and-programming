from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from helpers import data
from helpers import terminal

from .manager import AppManager


__all__ = ["MenuOption", "Menu"]


@dataclass(frozen=True)
class MenuOption:
    """Menu option

    Args:
        text (str): text to be printed in the menu
        call (Callable): call to be run when selected
        print_result (bool, optional): whether to print the returned result. Defaults to False.
    """

    text: str
    call: Callable
    print_result: bool = False

    def __str__(self) -> str:
        return self.text


class Menu:
    """Menu class"""

    def __init__(self) -> None:
        self.manager: AppManager = AppManager()
        self.__options: list[MenuOption] = []
        self.__populate_options()

    def __populate_options(self) -> None:
        """Internal: Populates the option list"""
        self.__options.append(
            MenuOption(
                "Load sample data",
                lambda: self.manager.load_json(data.load_sample()),
            ),
        )
        self.__options.append(
            MenuOption(
                "List students",
                lambda: self.manager.get_students(),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "List labs",
                lambda: self.manager.get_labs(),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Add student",
                lambda: self.manager.add_student(terminal.read_student()),
            ),
        )
        self.__options.append(
            MenuOption(
                "Search student by ID",
                lambda: self.manager.get_student_by_id(terminal.read_int("Enter ID: ")),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Search student by name",
                lambda: self.manager.search_student_by_name(input("Enter name: ")),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Search student by group",
                lambda: self.manager.search_student_by_group(
                    terminal.read_int("Enter group: "),
                ),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Add lab",
                lambda: self.manager.add_lab(terminal.read_lab()),
            ),
        )
        self.__options.append(
            MenuOption(
                "Search lab by ID",
                lambda: self.manager.get_lab_by_id(terminal.read_int("Enter ID: ")),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Search lab by description",
                lambda: self.manager.search_lab_by_description(
                    input("Enter description: "),
                ),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Exit",
                exit,
            ),
        )

    def __get_menu_text(self) -> str:
        """Internal: Returns a string representation of the menu text

        Returns:
            menu_text (str): string representation of the menu
        """
        str = ""
        for i, option in enumerate(self.__options, 1):
            str += f"{i}. {option}\n"
        return str

    def __call_option(self, opt: int) -> None:
        """Calls the function for the option

        Args:
            opt (int): ID of the option (indexed from 0)
        """
        terminal.clear()
        if opt not in range(len(self.__options)):
            terminal.print_wait("Invalid option specified. Press any key to continue.")
            return

        try:
            res = self.__options[opt].call()
        except ValueError as err:
            terminal.print_wait(f"\nError: {err}. Press any key to continue.")
            return

        if self.__options[opt].print_result:
            if isinstance(res, list):
                for x in res:
                    print(str(x))
            else:
                print(str(res))
            terminal.print_wait("\nPress any key to continue.")

    def run(self) -> None:
        """Runs the menu"""
        terminal.clear()
        while True:
            print(self.__get_menu_text())
            opt = terminal.read_int("Enter your selection: ")
            self.__call_option(opt - 1)
            terminal.clear()
