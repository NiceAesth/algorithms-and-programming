from __future__ import annotations

from dataclasses import dataclass

__all__ = ["Student"]


@dataclass
class Student:
    sid: int
    name: str
    group: int

    @classmethod
    def from_type(cls, obj: Student | dict) -> Student:
        """Converts a dict to a Student object

        Args:
            obj (Student | dict): Student object or dict

        Returns:
            Student: Student object
        """
        if isinstance(obj, cls):
            return obj
        return cls(**obj)

    def __str__(self) -> str:
        return f"Student {self.sid}: {self.name} in group {self.group}"
