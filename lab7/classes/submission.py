from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Submission:
    sid: int
    lid: int
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
