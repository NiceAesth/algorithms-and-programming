from __future__ import annotations
import math
import numbers
from dataclasses import dataclass
from typing import Any

__all__ = ["ComplexNumber", "ComplexType"]


@dataclass
class ComplexNumber:
    real: numbers.Real
    imag: numbers.Real

    @classmethod
    def from_type(cls, x):
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
        if isinstance(x, numbers.Real):
            return ComplexNumber(x, 0)
        raise TypeError(f"Type of value is {type(x)}. Expected: {ComplexType}")

    @staticmethod
    def ensure_type(func) -> function:
        """Function wrapper for ComplexNumber casting

        Args:
            func (Callable): function to be wrapped

        Returns:
            function: wrapped function with ComplexType to ComplexNumber casting
        """

        def _ensure_type(*args, **kwargs) -> Any:
            safe_args = args[0], ComplexNumber.from_type(args[1])
            return func(*safe_args, **kwargs)

        return _ensure_type

    def __abs__(self) -> int:
        return math.sqrt(self.real**2 + self.imag**2)

    def __int__(self) -> int:
        return int(self.__abs__())

    def __round__(self, n: int) -> ComplexNumber:
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

    def __trunc__(self) -> ComplexNumber:
        new_real = math.trunc(self.real)
        new_imag = math.trunc(self.imag)
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __add__(self, __o: ComplexNumber | tuple[int, int] | int) -> ComplexNumber:
        new_real = self.real + __o.real
        new_imag = self.imag + __o.imag
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __sub__(self, __o: ComplexType) -> ComplexNumber:
        new_real = self.real - __o.real
        new_imag = self.imag - __o.imag
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __mul__(self, __o: ComplexType) -> ComplexNumber:
        new_real = self.real * __o.real - self.imag * __o.imag
        new_imag = self.real * __o.imag + self.imag * __o.real
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __floordiv__(self, __o: ComplexType) -> ComplexNumber:
        return math.floor(self / __o)

    @ensure_type
    def __truediv__(self, __o: ComplexType) -> ComplexNumber:
        new_real = (self.real * __o.real + self.imag * __o.imag) / (
            __o.real**2 + __o.imag**2
        )
        new_imag = (self.imag * __o.real - self.real * __o.imag) / (
            __o.real**2 + __o.imag**2
        )
        return ComplexNumber(new_real, new_imag)

    @ensure_type
    def __lt__(self, __o: ComplexType) -> bool:
        return abs(self) < abs(__o)

    @ensure_type
    def __le__(self, __o: ComplexType) -> bool:
        return abs(self) < abs(__o) or self == __o

    @ensure_type
    def __gt__(self, __o: ComplexType) -> bool:
        return abs(self) > abs(__o)

    @ensure_type
    def __ge__(self, __o: ComplexType) -> bool:
        return abs(self) > abs(__o) or self == __o

    @ensure_type
    def __eq__(self, __o: ComplexType) -> bool:
        return self.real == __o.real and self.imag == __o.imag

    @ensure_type
    def __ne__(self, __o: ComplexType) -> bool:
        return not self == __o

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real} + {self.imag}i)"

    def __str__(self) -> str:
        return f"({self.real} + {self.imag}i)"


ComplexType = ComplexNumber | tuple[int, int] | int
