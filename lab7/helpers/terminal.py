from __future__ import annotations

import os
from typing import Any

from classes.lab import Lab
from classes.student import Student

__all__ = ["clear", "read_int", "read_subseq", "print_wait"]


def clear() -> None:
    """Clears the terminal.
    Clears the terminal based on the host OS.
    Return NoneType
    """
    os.system("cls" if os.name == "nt" else "clear")


def read_int(text: str = "") -> int:
    try:
        x = int(input(text))
    except:
        print("Invalid value specified. Try again.")
        x = read_int(text)
    return x


def read_student() -> Student:
    sid: int = read_int("Enter ID: ")
    name = input("Enter name: ")
    group = read_int("Enter group: ")
    return Student(sid, name, group)


def read_lab() -> Lab:
    lid = read_int("Enter ID: ")
    description = input("Enter description: ")
    deadline = read_int("Enter deadline: ")
    return Lab(lid, description, deadline)


def print_wait(*args: Any, **kwargs: Any) -> None:
    print(*args, **kwargs)
    input()
