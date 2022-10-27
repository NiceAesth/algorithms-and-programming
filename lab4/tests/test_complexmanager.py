from __future__ import annotations

import pytest
from classes import ComplexManager
from classes import ComplexNumber


def check_abs(x: ComplexNumber) -> bool:
    """Simple function to check if abs(x) < 10

    Args:
        x (ComplexNumber): number to be checked

    Returns:
        check (bool): True if abs(x) < 10 and False otherwise
    """
    return abs(x) < 10


SampleType = list[list[int]]


@pytest.fixture
def sample_data() -> SampleType:
    return [[1, 0], [0, 1], [10, 0], [3, 1], [2, 2], [15, 6], [13, 11], [60, 5]]


def test_load_json(sample_data: SampleType) -> None:
    """
    +----------------------+--------+
    | Input (sample_data)  | Output |
    +----------------------+--------+
    | manager.count        |      8 |
    +----------------------+--------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    assert manager.count == 8


def test_add_number() -> None:
    """
    +----------------------------------------+--------+
    | Input (ComplexNumber(5, 3), 5, (5, 3)) | Output |
    +----------------------------------------+--------+
    | manager.count                          |      3 |
    +----------------------------------------+--------+
    """
    manager = ComplexManager()
    manager.add_number(ComplexNumber(5, 3))
    manager.add_number(5)
    manager.add_number((5, 3))
    assert manager.count == 3


def test_remove_pos_number(sample_data: SampleType) -> None:
    """
    +------------------------------------------+--------+
    |           Input (sample_data)            | Output |
    +------------------------------------------+--------+
    | ComplexNumber(60, 5) not in manager.nlist | False  |
    +------------------------------------------+--------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    assert ComplexNumber(60, 5) in manager.nlist
    manager.remove_pos_number(7)
    assert ComplexNumber(60, 5) not in manager.nlist


def test_remove_seq_number(sample_data: SampleType) -> None:
    """
    +----------------------+--------+
    | Input (sample_data)  | Output |
    +----------------------+--------+
    | manager.count        |      0 |
    +----------------------+--------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    assert manager.count > 0
    manager.remove_seq_number(0, manager.count)
    assert manager.count == 0


def test_replace_number(sample_data: SampleType) -> None:
    """
    +------------------------------------------+--------+
    |           Input (sample_data)            | Output |
    +------------------------------------------+--------+
    | ComplexNumber(60, 5) not in manager.nlist | False  |
    | ComplexNumber(120, 3) in manager.nlist    | True   |
    +------------------------------------------+--------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    a, b = ComplexNumber(60, 5), ComplexNumber(120, 3)
    assert a in manager.nlist
    manager.replace_number(a, b)
    assert a not in manager.nlist
    assert b in manager.nlist


def test_sum_seq(sample_data: SampleType) -> None:
    """
    +-----------------------+---------------------+
    |  Input (sample_data)  |       Output        |
    +-----------------------+---------------------+
    | manager.sum_seq(0, 2) | ComplexNumber(1, 1) |
    +-----------------------+---------------------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    assert manager.sum_seq(0, 2) == ComplexNumber(1, 1)


def test_prod_seq(sample_data: SampleType) -> None:
    """
    +------------------------+---------------------+
    |  Input (sample_data)   |       Output        |
    +------------------------+---------------------+
    | manager.prod_seq(0, 2) | ComplexNumber(0, 1) |
    +------------------------+---------------------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    assert manager.prod_seq(0, 2) == ComplexNumber(0, 1)


def test_get_by_check(sample_data: SampleType) -> None:
    """
    +---------------------+--------+
    | Input (sample_data) | Output |
    +---------------------+--------+
    | len(resp)           |      4 |
    +---------------------+--------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    resp = manager.get_by_check(check_abs)
    assert len(resp) == 4


def test_filter_by_check(sample_data: SampleType) -> None:
    """
    +----------------------+--------+
    | Input (sample_data)  | Output |
    +----------------------+--------+
    | manager.count        |      4 |
    +----------------------+--------+
    """
    manager = ComplexManager()
    manager.load_json(sample_data)
    manager.filter_by_check(check_abs)
    assert manager.count == 4
