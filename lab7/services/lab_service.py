from __future__ import annotations

from entities import Lab
from entities import Problem
from repository import LabRepository


class LabService:
    """Service for lab operations."""

    def __init__(self, lab_repository: LabRepository) -> None:
        """Initialize the lab service.

        Args:
            lab_repository (LabRepository): lab repository
        """
        self.__repository = lab_repository

    @property
    def lab_count(self) -> int:
        """Returns the number of labs.

        Returns:
            int: number of labs
        """
        return self.__repository.lab_count

    @property
    def problem_count(self) -> int:
        """Returns the number of problems.

        Returns:
            int: number of problems
        """
        return self.__repository.problem_count

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__repository.load_json(obj)

    def get_labs(self) -> list[Lab]:
        """Returns a list of all labs

        Returns:
            list[Lab]: list of all labs
        """
        return self.__repository.get_labs()

    def get_lab_by_id(self, lid: int) -> Lab | None:
        """Returns a lab with the given ID

        Args:
            lid (int): ID of the lab

        Returns:
            lab (Lab): Lab with the given ID
        """
        return self.__repository.get_lab_by_id(lid)

    def add_lab(self, obj: Lab | dict) -> Lab:
        """Adds a lab to the list

        Args:
            obj (Lab | dict): lab data

        Returns:
            Lab: the added lab
        """
        return self.__repository.add_lab(obj)

    def delete_lab(self, obj: Lab | dict) -> None:
        """Deletes a lab from the list

        Args:
            obj (Lab | dict): lab data
        """
        self.__repository.delete_lab(obj)

    def delete_lab_by_id(self, lid: int) -> None:
        """Deletes a lab from the list

        Args:
            lid (int): ID of the lab
        """
        self.__repository.delete_lab(self.get_lab_by_id(lid))

    def get_problems(self) -> list[Problem]:
        """Returns a list of all problems

        Returns:
            list[Problem]: list of all problems
        """
        return self.__repository.get_problems()

    def get_problem_by_ids(self, lid: int, pid: int) -> Problem | None:
        """Returns a problem with the given ID

        Args:
            lid (int): ID of the lab
            pid (int): ID of the problem

        Returns:
            Problem (Problem): Problem with the given ID
        """
        return self.__repository.get_problem_by_ids(lid, pid)

    def add_problem(self, lid: int, obj: Problem | dict) -> Problem:
        """Adds a problem to the list

        Args:
            obj (Problem | dict): problem data

        Returns:
            Problem: the added problem
        """
        return self.__repository.add_problem(lid, obj)

    def search_problem_by_description(self, description: str) -> list[Problem]:
        """Searches for a problem by description

        Args:
            description (str): description of the problem

        Returns:
            list[Problem]: list of problems with the given description
        """
        return self.__repository.search_problem_by_description(description)

    def delete_problem_by_ids(self, lid: int, pid: int) -> None:
        """Deletes a problem from the list by IDs

        Args:
            lid (int): lab ID
            pid (int): problem ID
        """
        self.__repository.delete_problem_by_ids(lid, pid)
