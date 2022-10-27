from __future__ import annotations

import math

from classes import ComplexNumber


def test_eq() -> None:
    """
    +--------------------------------------------+--------+
    |                Input (x, y)                | Output |
    +--------------------------------------------+--------+
    | ComplexNumber(1, 0) == ComplexNumber(1, 0) | True   |
    | ComplexNumber(1, 0) == 1                   | True   |
    | ComplexNumber(1, 0) == (1, 0)              | True   |
    | ComplexNumber(1, 0) != 0                   | True   |
    +--------------------------------------------+--------+
    """
    assert ComplexNumber(1, 0) == ComplexNumber(1, 0)
    assert ComplexNumber(1, 0) == 1
    assert ComplexNumber(1, 0) == (1, 0)
    assert ComplexNumber(1, 0) != 0


def test_lt() -> None:
    """
    +--------------------------------------------+--------+
    |                Input (x, y)                | Output |
    +--------------------------------------------+--------+
    | ComplexNumber(5, 3) < ComplexNumber(5, 4)  | True   |
    | ComplexNumber(5, 3) < 10                   | True   |
    | ComplexNumber(5, 3) < (5, 4)               | False  |
    | ComplexNumber(5, 3) <= ComplexNumber(5, 3) | True   |
    +--------------------------------------------+--------+
    """
    a, b, c, d = ComplexNumber(5, 3), ComplexNumber(5, 4), 10, (1, 2)
    assert a < b
    assert a < c
    assert not a < d
    assert a <= a


def test_gt() -> None:
    """
    +--------------------------------------------+--------+
    |                Input (x, y)                | Output |
    +--------------------------------------------+--------+
    | ComplexNumber(5, 3) > ComplexNumber(3, 1)  | True   |
    | ComplexNumber(5, 3) > 3                    | True   |
    | ComplexNumber(5, 3) > (25, 2)              | False  |
    | ComplexNumber(5, 3) >= ComplexNumber(5, 3) | True   |
    +--------------------------------------------+--------+
    """
    a, b, c, d = ComplexNumber(5, 3), ComplexNumber(3, 1), 3, (25, 2)
    assert a > b
    assert a > c
    assert not a > d
    assert a >= a


def test_add() -> None:
    """
    +-------------------------------------------+----------------------+
    |               Input (x, y)                |        Output        |
    +-------------------------------------------+----------------------+
    | ComplexNumber(5, 3) + ComplexNumber(3, 6) | ComplexNumber(8, 9)  |
    | ComplexNumber(5, 3) + 10                  | ComplexNumber(15, 3) |
    | ComplexNumber(5, 3) + (1, 2)              | ComplexNumber(6, 5)  |
    +-------------------------------------------+----------------------+
    """
    a, b, c, d = ComplexNumber(5, 3), ComplexNumber(3, 6), 10, (1, 2)
    assert a + b == ComplexNumber(8, 9)
    assert a + c == ComplexNumber(15, 3)
    assert a + d == ComplexNumber(6, 5)


def test_subtract() -> None:
    """
    +-------------------------------------------+----------------------+
    |               Input (x, y)                |        Output        |
    +-------------------------------------------+----------------------+
    | ComplexNumber(5, 3) - ComplexNumber(3, 6) | ComplexNumber(2, -3) |
    | ComplexNumber(5, 3) - 10                  | ComplexNumber(-5, 3) |
    | ComplexNumber(5, 3) - (1, 2)              | ComplexNumber(4, 1)  |
    +-------------------------------------------+----------------------+
    """
    a, b, c, d = ComplexNumber(5, 3), ComplexNumber(3, 6), 10, (1, 2)
    assert a - b == ComplexNumber(2, -3)
    assert a - c == ComplexNumber(-5, 3)
    assert a - d == ComplexNumber(4, 1)


def test_floordiv() -> None:
    """
    +---------------------------------------------+----------------------+
    |                Input (x, y)                 |        Output        |
    +---------------------------------------------+----------------------+
    | ComplexNumber(25, 5) // ComplexNumber(5, 2) | ComplexNumber(4, -1) |
    | ComplexNumber(25, 5) // 3                   | ComplexNumber(8, 1)  |
    | ComplexNumber(25, 5) // (5, 2)              | ComplexNumber(4, -1) |
    +---------------------------------------------+----------------------+
    """
    a, b, c, d = ComplexNumber(25, 5), ComplexNumber(5, 2), 3, (5, 2)
    assert a // b == ComplexNumber(4, -1)
    assert a // c == ComplexNumber(8, 1)
    assert a // d == ComplexNumber(4, -1)


def test_truediv() -> None:
    """
    +--------------------------------------------+---------------------+
    |                Input (x, y)                |       Output        |
    +--------------------------------------------+---------------------+
    | ComplexNumber(25, 5) / ComplexNumber(5, 1) | ComplexNumber(5, 0) |
    | ComplexNumber(25, 5) / 5                   | ComplexNumber(5, 1) |
    | ComplexNumber(25, 5) / (5, 1)              | ComplexNumber(5, 0) |
    +--------------------------------------------+---------------------+
    """
    a, b, c, d = ComplexNumber(25, 5), ComplexNumber(5, 1), 5, (5, 1)
    assert a / b == ComplexNumber(5, 0)
    assert a / c == ComplexNumber(5, 1)
    assert a / d == ComplexNumber(5, 0)


def test_multiply() -> None:
    """
    +--------------------------------------------+------------------------+
    |                Input (x, y)                |         Output         |
    +--------------------------------------------+------------------------+
    | ComplexNumber(25, 5) * ComplexNumber(5, 1) | ComplexNumber(120, 50) |
    | ComplexNumber(25, 5) * 5                   | ComplexNumber(125, 25) |
    | ComplexNumber(25, 5) * (5, 1)              | ComplexNumber(120, 50) |
    +--------------------------------------------+------------------------+
    """
    a, b, c, d = ComplexNumber(25, 5), ComplexNumber(5, 1), 5, (5, 1)
    assert a * b == ComplexNumber(120, 50)
    assert a * c == ComplexNumber(125, 25)
    assert a * d == ComplexNumber(120, 50)


def test_abs() -> None:
    """
    +----------------------+-------------+
    |      Input (x)       |   Output    |
    +----------------------+-------------+
    | ComplexNumber(5, 0)  | abs(x) == 5 |
    | ComplexNumber(0, 0)  | abs(x) == 5 |
    | ComplexNumber(3, 4)  | abs(x) == 5 |
    | ComplexNumber(3, -4) | abs(x) == 5 |
    +----------------------+-------------+
    """
    a, b, c, d = (
        ComplexNumber(5, 0),
        ComplexNumber(0, 5),
        ComplexNumber(3, 4),
        ComplexNumber(3, -4),
    )
    assert abs(a) == 5
    assert abs(b) == 5
    assert abs(c) == 5
    assert abs(d) == 5


def test_int() -> None:
    """
    +----------------------+-------------+
    |      Input (x)       |   Output    |
    +----------------------+-------------+
    | ComplexNumber(5, 0)  | int(x) == 5 |
    | ComplexNumber(0, 0)  | int(x) == 5 |
    | ComplexNumber(3, 4)  | int(x) == 5 |
    | ComplexNumber(3, -4) | int(x) == 5 |
    +----------------------+-------------+
    """
    a, b, c, d = (
        ComplexNumber(5, 0),
        ComplexNumber(0, 5),
        ComplexNumber(3, 4),
        ComplexNumber(3, -4),
    )
    assert int(a) == 5
    assert int(b) == 5
    assert int(c) == 5
    assert int(d) == 5


def test_round() -> None:
    """
    +---------------------------+------------------------------------------+
    |         Input (x)         |                  Output                  |
    +---------------------------+------------------------------------------+
    | ComplexNumber(5.32, 2.13) | round(x, 0) == ComplexNumber(5, 2)       |
    | ComplexNumber(5.32, 2.13) | round(x, 1) == ComplexNumber(5.3, 2.1)   |
    | ComplexNumber(5.32, 2.13) | round(x, 2) == ComplexNumber(5.32, 2.13) |
    +---------------------------+------------------------------------------
    """
    a = ComplexNumber(5.32, 2.13)
    assert round(a, 0) == ComplexNumber(5, 2)
    assert round(a, 1) == ComplexNumber(5.3, 2.1)
    assert round(a, 2) == ComplexNumber(5.32, 2.13)


def test_floor() -> None:
    """
    +---------------------------+---------------------------------+
    |         Input (x)         |             Output              |
    +---------------------------+---------------------------------+
    | ComplexNumber(5.32, 2.13) | floor(x) == ComplexNumber(5, 2) |
    +---------------------------+---------------------------------+
    """
    a = ComplexNumber(5.32, 2.13)
    assert math.floor(a) == ComplexNumber(5, 2)


def test_ceil() -> None:
    """
    +---------------------------+--------------------------------+
    |         Input (x)         |             Output             |
    +---------------------------+--------------------------------+
    | ComplexNumber(5.32, 2.13) | ceil(x) == ComplexNumber(6, 3) |
    +---------------------------+--------------------------------+
    """
    a = ComplexNumber(5.32, 2.13)
    assert math.ceil(a) == ComplexNumber(6, 3)
