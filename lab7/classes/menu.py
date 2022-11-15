from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from helpers import data
from helpers import terminal

from .lab import LabManager
from .student import StudentManager


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
        self.student_manager: StudentManager = StudentManager()
        self.lab_manager: LabManager = LabManager()
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
        if 0 <= opt <= len(self.__options) - 1:
            res = self.__options[opt].call()
            if self.__options[opt].print_result:
                print(f"\n{res}\n")
                terminal.print_wait("Press any key to continue.")
        else:
            terminal.print_wait("Invalid option specified. Press any key to continue.")

    def run(self) -> None:
        """Runs the menu"""
        terminal.clear()
        while True:
            print(self.__get_menu_text())
            opt = terminal.read_int("Enter your selection: ")
            self.__call_option(opt - 1)
            terminal.clear()
