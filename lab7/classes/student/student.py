from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Student:
    sid: int
    name: str
    group: int
