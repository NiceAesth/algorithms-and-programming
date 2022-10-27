from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from helpers import data
from helpers import numbers
from helpers import terminal

from .complexmanager import ComplexManager

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
        self.manager: ComplexManager = ComplexManager()
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
                "Append a complex number to the list",
                lambda: self.manager.add_number(
                    terminal.read_complex("Enter the number: "),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Add a complex number to a position in the list",
                lambda: self.manager.add_number(
                    terminal.read_complex("Enter the number: "),
                    terminal.read_int("Enter the position: "),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Remove a complex number from the list",
                lambda: self.manager.remove_pos_number(
                    terminal.read_int("Enter the position of the number: "),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Remove a subsequence from the list",
                lambda: self.manager.remove_seq_number(
                    terminal.read_int("Enter the start position: "),
                    terminal.read_int("Enter the end position: "),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Replace all occurances of a number in the list",
                lambda: self.manager.replace_number(
                    terminal.read_complex("Enter the number to be replaced: "),
                    terminal.read_complex("Enter the replacement: "),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Print the imaginary part of elements in a subsequence",
                lambda: [x.imag for x in terminal.read_subseq(self.manager.nlist)],
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Print all elements with an abs lower than 10",
                lambda: self.manager.get_by_check(lambda x: abs(x) < 10),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Print all elements with an abs equal to 10",
                lambda: self.manager.get_by_check(lambda x: abs(x) == 10),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Get the sum of a subsequence",
                lambda: self.manager.sum_seq(
                    terminal.read_int("Enter the start position: "),
                    terminal.read_int("Enter the end position: "),
                ),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Get the product of a subsequence",
                lambda: self.manager.prod_seq(
                    terminal.read_int("Enter the start position: "),
                    terminal.read_int("Enter the end position: "),
                ),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Print the list sorted by the imaginary part descending",
                lambda: sorted(self.manager.nlist, reverse=True, key=lambda x: x.imag),
                True,
            ),
        )
        self.__options.append(
            MenuOption(
                "Filter numbers with a prime real part",
                lambda: self.manager.filter_by_check(
                    lambda x: not numbers.check_prime(x.real),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Filter numbers with abs < a given value",
                lambda: (
                    chk := terminal.read_int("Enter the number: "),
                    self.manager.filter_by_check(lambda x: abs(x) > chk),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Filter numbers with abs == a given value",
                lambda: (
                    chk := terminal.read_int("Enter the number: "),
                    self.manager.filter_by_check(lambda x: abs(x) != chk),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Filter numbers with abs > a given value",
                lambda: (
                    chk := terminal.read_int("Enter the number: "),
                    self.manager.filter_by_check(lambda x: abs(x) < chk),
                ),
            ),
        )
        self.__options.append(
            MenuOption(
                "Undo the last change to the list",
                self.manager.undo,
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
        if 0 <= opt <= len(self.__options):
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
