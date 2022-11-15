from __future__ import annotations

import os
from typing import Any

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


def read_subseq(list: list) -> list:
    start = read_int("Enter the start position: ")
    end = read_int("Enter the end position: ")
    try:
        return list[start:end]
    except:
        print("Invalid start and end provided. Try again.")
        return read_subseq(list)


def print_wait(*args: Any, **kwargs: Any) -> None:
    print(*args, **kwargs)
    input()
