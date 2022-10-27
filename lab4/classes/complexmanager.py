from __future__ import annotations
from typing import Any, Callable
from . import ComplexNumber, ComplexType

__all__ = ["ComplexManager"]


class ComplexManager:
    def __init__(self) -> None:
        self._list = list()
        self._prev = list()

    @property
    def list(self):
        """List of ComplexNumber types"""
        return self._list

    @property
    def count(self):
        """Number of elements in _list"""
        return len(self._list)

    def undo(self) -> None:
        """Undoes the latest change to the list (undo history of 1)"""
        self._list = self._prev.copy()

    @staticmethod
    def updates_list(func) -> function:
        """Function wrapper for undo functionality. Use on functions which modify _list

        Args:
            func (Callable): function to be wrapped

        Returns:
            function: wrapped function with _prev updating
        """

        def _updates_list(*args, **kwargs) -> Any:
            args[0]._prev = args[0]._list.copy()
            return func(*args, **kwargs)

        return _updates_list

    @updates_list
    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self._list.clear()
        for x in obj:
            self._list.append(ComplexNumber(*x))

    @updates_list
    def add_number(self, x: ComplexType, pos: int = -1) -> None:
        """Adds a number to _list

        Args:
            x (ComplexType): value to be added
            pos (int, optional): position to insert in. Defaults to appending to the list.
        """
        x = ComplexNumber.from_type(x)
        if pos < 0:
            pos = len(self._list)
        self._list.insert(pos, x)

    @updates_list
    def remove_pos_number(self, pos: int) -> None:
        """Removes a number from _list

        Args:
            pos (int): position of the element to be removed
        """
        del self._list[pos]

    @updates_list
    def remove_seq_number(self, start: int, end: int) -> None:
        """Removes a sequence of numbers from _list

        Args:
            start (int): start position of the sequence
            end (int): end position of the sequence
        """
        del self._list[start:end]

    @updates_list
    def replace_number(self, x: ComplexType, y: ComplexType) -> None:
        """Replaces a number in _list

        Args:
            x (ComplexType): number to be replaced
            y (ComplexType): number to replace with
        """
        x = ComplexNumber.from_type(x)
        y = ComplexNumber.from_type(y)
        self._list = [y if i == x else i for i in self._list]

    def get_by_check(self, check: Callable) -> list[ComplexNumber]:
        """Get a list of elements that pass a given check

        Args:
            check (Callable): check function. Should take ComplexNumber as argument. Expected return is bool.

        Returns:
            list[ComplexNumber]: list of numbers where check(x) is True
        """
        return [x for x in self._list if check(x)]

    @updates_list
    def filter_by_check(self, check: Callable) -> None:
        """Removes elements which do not pass a given check from the list

        Args:
            check (Callable): check function. Should take ComplexNumber as argument. Expected return is bool.
        """
        self._list = self.get_by_check(check)

    def sum_seq(self, start: int, end: int) -> ComplexNumber:
        """Get the sum of a sequence

        Args:
            start (int): start position of the sequence
            end (int): end position of the sequence

        Returns:
            ComplexNumber: sum of the elements in _list[start:end]
        """
        res = ComplexNumber(0, 0)
        for x in self._list[start:end]:
            res += x
        return res

    def prod_seq(self, start: int, end: int) -> ComplexNumber:
        """Get the product of a sequence

        Args:
            start (int): start position of the sequence
            end (int): end position of the sequence

        Returns:
            ComplexNumber: product of the elements in _list[start:end]
        """
        res = ComplexNumber(1, 0)
        for x in self._list[start:end]:
            res *= x
        return res
