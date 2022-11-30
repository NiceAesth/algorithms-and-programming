from __future__ import annotations

import dataclasses
import json

from entities import Lab
from entities import Problem
from helpers.data import DateTimeEncoder


class LabRepository:
    """Repository for lab operations."""

    def __init__(self) -> None:
        """Initialize the lab repository."""
        self.__labs = []

    @property
    def lab_count(self) -> int:
        """Returns the number of labs.

        Returns:
            int: number of labs
        """
        return len(self.__labs)

    @property
    def problem_count(self) -> int:
        """Returns the number of problems.

        Returns:
            int: number of problems
        """
        return len(self.get_problems())

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__labs.clear()
        for x in obj:
            self.__labs.append(Lab.from_type(x))

    def get_labs(self) -> list[Lab]:
        """Gets the list of all labs

        Returns:
            list[Lab]: list of labs
        """
        return self.__labs

    def get_lab_by_id(self, lid: int) -> Lab | None:
        """Returns a lab with the given ID

        Args:
            lid (int): ID of the lab

        Returns:
            lab (Lab): Lab with the given ID
        """
        for lab in self.__labs:
            if lab.lid == lid:
                return lab
        return None

    def add_lab(self, obj: Lab | dict) -> Lab:
        """Adds a lab to the list

        Args:
            obj (Lab | dict): lab data

        Returns:
            Lab: the added lab
        """
        lab = Lab.from_type(obj)
        if self.get_lab_by_id(lab.lid) is not None:
            raise ValueError("Lab with the given ID already exists")
        self.__labs.append(lab)
        return self.__labs[-1]

    def delete_lab(self, obj: Lab | dict) -> None:
        """Deletes a lab from the list

        Args:
            obj (Lab | dict): lab data
        """
        self.__labs.remove(Lab.from_type(obj))

    def delete_lab_by_id(self, lid: int) -> None:
        """Deletes a lab from the list by ID

        Args:
            lid (int): lab ID
        """
        self.__labs.remove(self.get_lab_by_id(lid))

    def get_problems(self) -> list[Problem]:
        """Gets the list of all problems

        Returns:
            list[Problem]: list of problems
        """
        return [x for lab in self.__labs for x in lab.problems]

    def get_problem_by_ids(self, lid: int, pid: int) -> Problem | None:
        """Returns a submission with the given ID

        Args:
            lid (int): ID of the lab
            pid (int): ID of the problem

        Returns:
            submission (Submission): Submission with the given ID
        """
        for lab in self.__labs:
            if lab.lid == lid:
                for problem in lab.problems:
                    if problem.pid == pid:
                        return problem
        return None

    def add_problem(self, lid: int, obj: Problem | dict) -> Problem:
        """Adds a problem to the list

        Args:
            lid (int): ID of the lab
            obj (Problem | dict): problem data

        Returns:
            Problem: the added problem
        """
        problem = Problem.from_type(obj)
        lab = self.get_lab_by_id(lid)
        if lab is None:
            raise ValueError("Lab with the given ID does not exist")
        if self.get_problem_by_ids(lid, problem.pid) is not None:
            raise ValueError("Problem with the given ID already exists")
        lab.problems.append(problem)
        return lab.problems[-1]

    def search_problem_by_description(self, description: str) -> list[Problem]:
        """Searches for problems with the given description

        Args:
            description (str): description of the problem

        Returns:
            problems (list[Problem]): list of problems with the given description
        """
        return [x for x in self.get_problems() if x.description == description]

    def delete_problem_by_ids(self, lid: int, pid: int) -> None:
        """Deletes a problem from the list by IDs

        Args:
            lid (int): lab ID
            pid (int): problem ID
        """
        for lab in self.__labs:
            if lab.lid == lid:
                lab.problems.remove(self.get_problem_by_ids(lid, pid))


class LabFileRepository(LabRepository):
    """Repository for lab operations using a file."""

    def __init__(self, filename: str) -> None:
        """Initialize the lab repository.

        Args:
            filename (str): name of the file
        """
        super().__init__()
        self.__filename = filename
        self.__load_file()

    def __load_file(self) -> None:
        """Loads the data from the file."""
        try:
            with open(self.__filename) as file:
                self.load_json(json.load(file))
        except FileNotFoundError:
            pass

    def __save_file(self) -> None:
        """Saves the data to the file."""
        with open(self.__filename, "w") as file:
            json.dump(
                [dataclasses.asdict(x) for x in self.get_labs()],
                file,
                indent=4,
                cls=DateTimeEncoder,
            )

    def add_lab(self, obj: Lab | dict) -> Lab:
        """Adds a lab to the list

        Args:
            obj (Lab | dict): lab data

        Returns:
            Lab: the added lab
        """
        lab = super().add_lab(obj)
        self.__save_file()
        return lab

    def delete_lab(self, obj: Lab | dict) -> None:
        """Deletes a lab from the list

        Args:
            obj (Lab | dict): lab data
        """
        super().delete_lab(obj)
        self.__save_file()

    def delete_lab_by_id(self, lid: int) -> None:
        """Deletes a lab from the list by ID

        Args:
            lid (int): lab ID
        """
        super().delete_lab_by_id(lid)
        self.__save_file()

    def add_problem(self, lid: int, obj: Problem | dict) -> Problem:
        """Adds a problem to the list

        Args:
            lid (int): ID of the lab
            obj (Problem | dict): problem data

        Returns:
            Problem: the added problem
        """
        problem = super().add_problem(lid, obj)
        self.__save_file()
        return problem

    def delete_problem_by_ids(self, lid: int, pid: int) -> None:
        """Deletes a problem from the list by IDs

        Args:
            lid (int): lab ID
            pid (int): problem ID
        """
        super().delete_problem_by_ids(lid, pid)
        self.__save_file()
