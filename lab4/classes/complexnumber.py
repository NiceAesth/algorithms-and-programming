from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import SupportsAbs
from typing import SupportsFloat
from typing import SupportsInt
from typing import SupportsRound

from typeguard import check_type

__all__ = ["Number", "ComplexType", "ComplexNumber"]


@dataclass
class ComplexNumber(SupportsAbs, SupportsFloat, SupportsInt, SupportsRound):
    real: Number
    imag: Number

    @classmethod
    def from_type(cls: Any, x: Any) -> ComplexNumber:
        """Casts an object to a ComplexNumber type

        Args:
            x (ComplexType): value to be cast to ComplexNumber

        Returns:
            x (ComplexNumber): a ComplexNumber object
        """
        if isinstance(x, cls):
            return x
        if isinstance(x, tuple):
            return ComplexNumber(*x)
        try:
            check_type("x", x, Number)
            return ComplexNumber(x, 0)
        except:
            raise TypeError(f"Type of value is {type(x)}. Expected: {ComplexType}")

    @staticmethod
    def ensure_type(func: Callable) -> function:
        """Function wrapper for ComplexNumber casting

        Args:
            func (Callable): function to be wrapped

        Returns:
            function: wrapped function with ComplexType to ComplexNumber casting
        """

        def _ensure_type(*args: Any, **kwargs: Any) -> Any:
            safe_args = args[0], ComplexNumber.from_type(args[1])
            return func(*safe_args, **kwargs)

        return _ensure_type

    def __abs__(self) -> float:
        return math.sqrt(self.real**2 + self.imag**2)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return int(self.__abs__())

    def __round__(self, n: int = 0) -> Any:
        new_real = round(self.real, n)
        new_imag = round(self.imag, n)
        return ComplexNumber(new_real, new_imag)

    def __floor__(self) -> ComplexNumber:
        new_real = math.floor(self.real)
        new_imag = math.floor(self.imag)
        return ComplexNumber(new_real, new_imag)

    def __ceil__(self) -> ComplexNumber:
        new_real = math.ceil(self.real)
        new_imag = math.ceil(self.imag)
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __add__(self, __o: ComplexNumber) -> ComplexNumber:
        new_real = self.real + __o.real
        new_imag = self.imag + __o.imag
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __sub__(self, __o: ComplexNumber) -> ComplexNumber:
        new_real = self.real - __o.real
        new_imag = self.imag - __o.imag
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __mul__(self, __o: ComplexNumber) -> ComplexNumber:
        new_real = self.real * __o.real - self.imag * __o.imag
        new_imag = self.real * __o.imag + self.imag * __o.real
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __floordiv__(self, __o: ComplexNumber) -> ComplexNumber:
        return math.floor(self / __o)  # type: ignore

    @ensure_type
    def __truediv__(self, __o: ComplexNumber) -> ComplexNumber:
        new_real = (self.real * __o.real + self.imag * __o.imag) / (
            __o.real**2 + __o.imag**2
        )
        new_imag = (self.imag * __o.real - self.real * __o.imag) / (
            __o.real**2 + __o.imag**2
        )
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __lt__(self, __o: ComplexNumber) -> bool:
        return abs(self) < abs(__o)

    @ensure_type
    def __le__(self, __o: ComplexNumber) -> bool:
        return abs(self) < abs(__o) or self == __o

    @ensure_type
    def __gt__(self, __o: ComplexNumber) -> bool:
        return abs(self) > abs(__o)

    @ensure_type
    def __ge__(self, __o: ComplexNumber) -> bool:
        return abs(self) > abs(__o) or self == __o

    def __eq__(self, __o: Any) -> bool:
        try:
            check_type("__o", __o, ComplexType)
        except:
            return NotImplemented
        x = ComplexNumber.from_type(__o)
        return self.real == x.real and self.imag == x.imag

    def __ne__(self, __o: Any) -> bool:
        try:
            check_type("__o", __o, ComplexType)
        except:
            return NotImplemented
        x = ComplexNumber.from_type(__o)
        return not self == x

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real} + {self.imag}i)"

    def __str__(self) -> str:
        return f"({self.real} + {self.imag}i)"


Number = int | float
ComplexType = ComplexNumber | tuple[Number, Number] | Number  # type: ignore
