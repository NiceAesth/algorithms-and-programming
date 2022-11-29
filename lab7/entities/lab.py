from __future__ import annotations

import datetime
from dataclasses import dataclass
from dataclasses import field

__all__ = ["Lab", "Problem"]


@dataclass
class Problem:
    """Problem class

    Attributes:
        pid (int): Problem ID
        description (str): Problem description
        deadline (datetime.datetime): Problem deadline
    """

    pid: int
    description: str
    deadline: datetime.datetime

    def __post_init__(self):
        """Enforces the deadline to be a datetime object"""
        if isinstance(self.deadline, str):
            self.deadline = datetime.datetime.fromisoformat(self.deadline)

    @classmethod
    def from_type(cls, obj: Problem | dict) -> Problem:
        """Converts a dict to a Problem object

        Args:
            obj (Problem | dict): Problem object or dict

        Returns:
            Problem: Problem object
        """
        if isinstance(obj, cls):
            return obj
        return cls(**obj)

    def __str__(self) -> str:
        return f"Problem {self.pid}: {self.description} with deadline {self.deadline}"


@dataclass
class Lab:
    """Lab class

    Attributes:
        lid (int): Lab ID
        problems (dict[int, Problem]): Lab problems
    """

    lid: int
    problems: list[Problem] = field(default_factory=list)

    def __post_init__(self):
        """Enforces the type of the problems list"""
        if isinstance(self.problems, list):
            self.problems = [Problem.from_type(x) for x in self.problems]

    def get_problem_by_id(self, pid: int) -> Problem | None:
        """Gets a problem by its ID

        Args:
            pid (int): Problem ID

        Returns:
            Problem | None: Problem object or None
        """
        for problem in self.problems:
            if problem.pid == pid:
                return problem
        return None

    @property
    def problem_count(self) -> int:
        """Returns the number of problems in the lab

        Returns:
            int: number of problems
        """
        return len(self.problems)

    @classmethod
    def from_type(cls, obj: Lab | dict) -> Lab:
        """Converts a dict to a Lab object

        Args:
            obj (Lab | dict): Lab object or dict

        Returns:
            Lab: Lab object
        """
        if isinstance(obj, cls):
            return obj
        return cls(**obj)

    def __str__(self) -> str:
        """Returns a string representation of the lab"""
        return f"Lab {self.lid}: {self.problem_count} problems"
