from __future__ import annotations

import datetime
from dataclasses import dataclass


@dataclass
class Lab:
    pid: int
    description: str
    deadline: datetime.datetime
