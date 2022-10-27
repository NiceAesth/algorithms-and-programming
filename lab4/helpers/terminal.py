from __future__ import annotations

import os
from typing import Any

from classes.complexnumber import ComplexNumber

__all__ = ["clear", "read_int", "read_complex", "read_subseq", "print_wait"]


def clear() -> None:
    """Clears the terminal.
    Clears the terminal based on the host OS.
    Return NoneType
    """
    os.system("cls" if os.name == "nt" else "clear")


def read_int(text: str = "") -> int:
    x = input(text)
    return int(x)


def read_complex(text: str = "") -> ComplexNumber:
    print(text)
    x = read_int("\tEnter the real part: ")
    y = read_int("\tEnter the imaginary part: ")
    return ComplexNumber(x, y)


def read_subseq(list: list) -> list:
    start = read_int("Enter the start position: ")
    end = read_int("Enter the end position: ")
    return list[start:end]


def print_wait(*args: Any, **kwargs: Any) -> None:
    print(*args, **kwargs)
    input()
