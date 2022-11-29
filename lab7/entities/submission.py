from __future__ import annotations

from dataclasses import dataclass

__all__ = ["Submission"]


@dataclass
class Submission:
    """Submission class

    Attributes:
        sid (int): Student ID
        pid (int): Problem ID
        grade (int): Grade, None if not graded
        submission_date (datetime.datetime): Submission date
    """

    sid: int
    lid: int
    pid: int
    grade: float | None

    @classmethod
    def from_type(cls, obj: Submission | dict) -> Submission:
        """Converts a dict to a Submission object

        Args:
            obj (Submission | dict): Submission object or dict

        Returns:
            Submission: Submission object
        """
        if isinstance(obj, cls):
            return obj
        return cls(**obj)
