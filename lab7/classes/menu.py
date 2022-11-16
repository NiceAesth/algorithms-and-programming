from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from helpers import data
from helpers import terminal

from .manager import AppManager


__all__ = ["MainMenu"]


@dataclass(frozen=True)
class MenuOption:
    """Menu option

    Attributes:
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

    def __init__(self, manager: AppManager, title: str = "Menu") -> None:
        self.title: str = title
        self.options: list[MenuOption] = []
        self.manager: AppManager = manager
        self.__running: bool = False

    def __populate_options(self) -> None:
        """Internal: Populates the option list"""
        raise NotImplementedError

    def __get_menu_text(self) -> str:
        """Internal: Returns a string representation of the menu text

        Returns:
            menu_text (str): string representation of the menu
        """
        str = f"{self.title}\n"
        for i, option in enumerate(self.options, 1):
            str += f"{i}. {option}\n"
        return str

    def __call_option(self, opt: int) -> None:
        """Calls the function for the option

        Args:
            opt (int): ID of the option (indexed from 0)
        """
        terminal.clear()
        if opt not in range(len(self.options)):
            terminal.print_wait("Invalid option specified. Press any key to continue.")
            return

        try:
            res = self.options[opt].call()
        except ValueError as err:
            terminal.print_wait(f"\nError: {err}. Press any key to continue.")
            return

        if self.options[opt].print_result:
            if isinstance(res, list):
                for x in res:
                    print(str(x))
            else:
                print(str(res))
            terminal.print_wait("\nPress any key to continue.")

    def run(self) -> None:
        """Runs the menu"""
        self.__running = True
        terminal.clear()
        while self.__running:
            print(self.__get_menu_text())
            opt = terminal.read_int("Enter your selection: ")
            self.__call_option(opt - 1)
            terminal.clear()

    def exit(self) -> None:
        """Exits the menu"""
        self.__running = False


class StudentMenu(Menu):
    """Student menu class"""

    def __init__(self, manager: AppManager) -> None:
        super().__init__(manager, "Manage students")
        self.__populate_options()

    def __populate_options(self) -> None:
        self.options.extend(
            (
                MenuOption(
                    "List students",
                    lambda: self.manager.get_students(),
                    True,
                ),
                MenuOption(
                    "Add student",
                    lambda: self.manager.add_student(terminal.read_student()),
                ),
                MenuOption(
                    "Search student by ID",
                    lambda: self.manager.get_student_by_id(
                        terminal.read_int("Enter ID: "),
                    ),
                    True,
                ),
                MenuOption(
                    "Search student by name",
                    lambda: self.manager.search_student_by_name(input("Enter name: ")),
                    True,
                ),
                MenuOption(
                    "Search student by group",
                    lambda: self.manager.search_student_by_group(
                        terminal.read_int("Enter group: "),
                    ),
                    True,
                ),
                MenuOption(
                    "Get failing students",
                    self.manager.get_failing_students,
                    True,
                ),
                MenuOption("Back", self.exit),
            ),
        )


class ProblemMenu(Menu):
    """Problem menu class"""

    def __init__(self, manager: AppManager) -> None:
        super().__init__(manager, "Manage problems")
        self.__populate_options()

    def __populate_options(self) -> None:
        self.options.extend(
            (
                MenuOption(
                    "Add problem",
                    lambda: self.manager.add_problem(*terminal.read_lab_problem()),
                ),
                MenuOption(
                    "Assign problem to student",
                    lambda: self.manager.assign_lab_problem(
                        terminal.read_int("Enter student ID: "),
                        terminal.read_int("Enter lab ID: "),
                        terminal.read_int("Enter problem ID: "),
                    ),
                ),
                MenuOption(
                    "Grade problem for student",
                    lambda: self.manager.assign_lab_problem(
                        terminal.read_int("Enter student ID: "),
                        terminal.read_int("Enter lab ID: "),
                        terminal.read_int("Enter problem ID: "),
                        terminal.read_int("Enter grade: "),
                    ),
                ),
                MenuOption(
                    "Search problem by ID",
                    lambda: self.manager.get_problem_by_ids(
                        terminal.read_int("Enter lab ID: "),
                        terminal.read_int("Enter ID: "),
                    ),
                    True,
                ),
                MenuOption(
                    "Search problem by description",
                    lambda: self.manager.search_problem_by_description(
                        input("Enter description: "),
                    ),
                    True,
                ),
                MenuOption("Back", self.exit),
            ),
        )


class LabMenu(Menu):
    """Lab menu class"""

    def __init__(self, manager: AppManager) -> None:
        super().__init__(manager, "Manage labs")
        self.__problem_menu = ProblemMenu(manager)
        self.__populate_options()

    def __populate_options(self) -> None:
        self.options.extend(
            (
                MenuOption(
                    "List labs",
                    lambda: self.manager.get_labs(),
                    True,
                ),
                MenuOption(
                    "Add lab",
                    lambda: self.manager.add_lab(terminal.read_lab()),
                ),
                MenuOption(
                    "Search lab by ID",
                    lambda: self.manager.get_lab_by_id(terminal.read_int("Enter ID: ")),
                    True,
                ),
                MenuOption(
                    "Manage problems",
                    self.__problem_menu.run,
                ),
                MenuOption(
                    "Get lab grades",
                    lambda: self.manager.get_lab_grades_str(
                        terminal.read_int("Enter lab ID: "),
                    ),
                    True,
                ),
                MenuOption("Back", self.exit),
            ),
        )


class MainMenu(Menu):
    """Main menu class"""

    def __init__(self, manager: AppManager) -> None:
        super().__init__(manager, "Main menu")
        self.__student_menu = StudentMenu(self.manager)
        self.__lab_menu = LabMenu(self.manager)
        self.__populate_options()

    def __populate_options(self) -> None:
        self.options.extend(
            (
                MenuOption(
                    "Load sample data",
                    lambda: self.manager.load_json(data.load_sample()),
                ),
                MenuOption(
                    "Manage students",
                    self.__student_menu.run,
                ),
                MenuOption(
                    "Manage labs",
                    self.__lab_menu.run,
                ),
                MenuOption("Exit", self.exit),
            ),
        )
