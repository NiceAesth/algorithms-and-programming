from __future__ import annotations

import datetime
from dataclasses import dataclass

__all__ = ["Lab"]


@dataclass
class Lab:
    lid: int
    description: str
    deadline: datetime.datetime

    def __post__init__(self):
        """Converts the deadline to a datetime object"""
        if isinstance(self.deadline, str):
            self.deadline = datetime.datetime.fromisoformat(self.deadline)

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
        return f"Lab {self.lid}: {self.description} (deadline: {self.deadline})"
