from __future__ import annotations

import datetime
import json

import pytest
from classes import AppManager
from classes import Lab
from classes import Problem
from classes import Student


@pytest.fixture
def sample_data() -> list:
    """Returns sample data for testing"""
    with open("data/sample.json") as f:
        return json.load(f)


def test_load_json(sample_data):
    """
    +--------------------------+--------+
    |          Input           | Output |
    +--------------------------+--------+
    | manager.student_count    |      5 |
    | manager.lab_count        |      2 |
    | manager.submission_count |      6 |
    +--------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert manager.student_count == 5
    assert manager.lab_count == 2
    assert manager.submission_count == 6


def test_get_students(sample_data):
    """Returns a list of students
    +---------------------------+--------+
    |           Input           | Output |
    +---------------------------+--------+
    | len(manager.get_students) |      5 |
    +---------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.get_students()) == 5


def test_get_student_by_id(sample_data):
    """
    +---------------------------+--------+
    |           Input           | Output |
    +---------------------------+--------+
    | get_student_by_id(1).name | "John" |
    | get_student_by_id(2).name | "Mary" |
    | get_student_by_id(3).name | "Peter"|
    | get_student_by_id(4).name | "Ann"  |
    | get_student_by_id(5).name | "Bob"  |
    | get_student_by_id(6)      | None   |
    +---------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert manager.get_student_by_id(1).name == "John"
    assert manager.get_student_by_id(2).name == "Mary"
    assert manager.get_student_by_id(3).name == "Peter"
    assert manager.get_student_by_id(4).name == "Ann"
    assert manager.get_student_by_id(5).name == "Bob"
    assert manager.get_student_by_id(6) is None


def test_get_failing_students(sample_data):
    """
    +-------------------------------------+--------+
    |                Input                | Output |
    +-------------------------------------+--------+
    | len(manager.get_failing_students()) |      1 |
    +-------------------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.get_failing_students()) == 1
    assert manager.get_failing_students()[0][0].name == "Bob"


def test_search_student_by_group(sample_data):
    """
    +-------------------------------------------+--------+
    |                Input                      | Output |
    +-------------------------------------------+--------+
    | len(manager.search_student_by_group(311)) |      2 |
    | len(manager.search_student_by_group(312)) |      2 |
    | len(manager.search_student_by_group(313)) |      1 |
    | len(manager.search_student_by_group(314)) |      0 |
    +-------------------------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.search_student_by_group(311)) == 2
    assert len(manager.search_student_by_group(312)) == 2
    assert len(manager.search_student_by_group(313)) == 1
    assert len(manager.search_student_by_group(314)) == 0


def test_search_student_by_name(sample_data):
    """
    +---------------------------------------------+--------+
    |                Input                        | Output |
    +---------------------------------------------+--------+
    | len(manager.search_student_by_name("John")) |      1 |
    | len(manager.search_student_by_name("Mary")) |      1 |
    | len(manager.search_student_by_name("Peter"))|      1 |
    | len(manager.search_student_by_name("Ann"))  |      1 |
    | len(manager.search_student_by_name("Bob"))  |      1 |
    | len(manager.search_student_by_name("Alice"))|      0 |
    +---------------------------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.search_student_by_name("John")) == 1
    assert len(manager.search_student_by_name("Mary")) == 1
    assert len(manager.search_student_by_name("Peter")) == 1
    assert len(manager.search_student_by_name("Ann")) == 1
    assert len(manager.search_student_by_name("Bob")) == 1
    assert len(manager.search_student_by_name("Alice")) == 0


def test_add_student(sample_data):
    """
    +---------------------------+--------+
    |           Input           | Output |
    +---------------------------+--------+
    | get_student_by_id(6).name | "Alice"|
    +---------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.add_student(Student(6, "Alice", 314))
    assert manager.student_count == 6
    assert manager.get_student_by_id(6).name == "Alice"


def test_delete_student_by_id(sample_data):
    """
    +----------------------+--------+
    |        Input         | Output |
    +----------------------+--------+
    | get_student_by_id(1) | None   |
    +----------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.delete_student_by_id(1)
    assert manager.student_count == 4
    assert manager.get_student_by_id(1) is None


def test_get_labs(sample_data):
    """
    +----------------------+--------+
    |        Input         | Output |
    +----------------------+--------+
    | len(manager.get_labs)|      2 |
    +----------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.get_labs()) == 2


def test_get_lab_by_id(sample_data):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | get_lab_by_id(1) | not None |
    | get_lab_by_id(2) | not None |
    | get_lab_by_id(3) | None     |
    +------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert manager.get_lab_by_id(1) is not None
    assert manager.get_lab_by_id(2) is not None
    assert manager.get_lab_by_id(3) is None


def test_add_lab(sample_data):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | manager.lab_count|        3 |
    +------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.add_lab(Lab(3))
    assert manager.lab_count == 3


def test_delete_lab_by_id(sample_data):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | manager.lab_count|        1 |
    +------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.delete_lab_by_id(1)
    assert manager.lab_count == 1
    assert manager.get_lab_by_id(1) is None


def test_get_problems(sample_data):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | len(manager.get_problems)|        5 |
    +--------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.get_problems()) == 5


def test_get_problem_by_ids(sample_data):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | get_problem_by_ids(1, 1) | not None |
    | get_problem_by_ids(1, 2) | not None |
    | get_problem_by_ids(1, 3) | not None |
    | get_problem_by_ids(2, 1) | not None |
    | get_problem_by_ids(2, 2) | not None |
    | get_problem_by_ids(2, 3) | None     |
    | get_problem_by_ids(3, 1) | None     |
    +--------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert manager.get_problem_by_ids(1, 1).description == "Problem 1"
    assert manager.get_problem_by_ids(1, 2).description == "Problem 2"
    assert manager.get_problem_by_ids(1, 3).description == "Problem 3"
    assert manager.get_problem_by_ids(2, 1).description == "Problem 1"
    assert manager.get_problem_by_ids(2, 2).description == "Problem 2"
    assert manager.get_problem_by_ids(2, 3) is None
    assert manager.get_problem_by_ids(3, 1) is None


def test_add_problem(sample_data):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | manager.problem_count    |        6 |
    +--------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.add_problem(1, Problem(4, "Problem 4", "2022-10-10"))
    problem = manager.get_problem_by_ids(1, 4)
    assert type(problem.deadline) is datetime.datetime
    assert manager.problem_count == 6


def test_search_problem_by_description(sample_data):
    """
    +--------------------------------------------------------+----------+
    |             Input                                      |  Output  |
    +--------------------------------------------------------+----------+
    | len(manager.search_problem_by_description("Problem 1"))|        2 |
    | len(manager.search_problem_by_description("Problem 2"))|        2 |
    | len(manager.search_problem_by_description("Problem 3"))|        1 |
    | len(manager.search_problem_by_description("Problem 4"))|        0 |
    +--------------------------------------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.search_problem_by_description("Problem 1")) == 2
    assert len(manager.search_problem_by_description("Problem 2")) == 2
    assert len(manager.search_problem_by_description("Problem 3")) == 1
    assert len(manager.search_problem_by_description("Problem 4")) == 0


def test_delete_problem_by_ids(sample_data):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | manager.problem_count    |        4 |
    +--------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.delete_problem_by_ids(1, 1)
    assert manager.get_problem_by_ids(1, 1) is None
    assert manager.problem_count == 4


def test_get_submissions(sample_data):
    """
    +-----------------------------+----------+
    |        Input                |  Output  |
    +-----------------------------+----------+
    | len(manager.get_submissions)|        6 |
    +-----------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.get_submissions()) == 6


def test_get_lab_submissions(sample_data):
    """
    +--------------------------------------+----------+
    |        Input                         |  Output  |
    +--------------------------------------+----------+
    | len(manager.get_lab_submissions(1))  |        5 |
    | len(manager.get_lab_submissions(2))  |        1 |
    | len(manager.get_lab_submissions(3))  |        0 |
    +--------------------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert len(manager.get_lab_submissions(1)) == 5
    assert len(manager.get_lab_submissions(2)) == 1
    assert len(manager.get_lab_submissions(3)) == 0


def test_assign_lab_problem(sample_data):
    """
    +------------------------------------+----------+
    |        Input                       |  Output  |
    +------------------------------------+----------+
    | len(manager.get_lab_submissions(1))|        6 |
    +------------------------------------+----------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    manager.assign_lab_problem(1, 1, 1)
    assert len(manager.get_lab_submissions(1)) == 5


def test_get_student_average(sample_data):
    """
    +--------------------------------+--------+
    |             Input              | Output |
    +--------------------------------+--------+
    | manager.get_student_average(1) | 10     |
    | manager.get_student_average(2) | 9.5    |
    | manager.get_student_average(3) | None   |
    | manager.get_student_average(4) | 8      |
    | manager.get_student_average(5) | 3.5    |
    | manager.get_student_average(6) | None   |
    +--------------------------------+--------+
    """
    manager = AppManager()
    manager.load_json(sample_data)
    assert manager.get_student_average(1) == 10
    assert manager.get_student_average(2) == 9.5
    assert manager.get_student_average(3) is None
    assert manager.get_student_average(4) == 8
    assert manager.get_student_average(5) == 3.5
    assert manager.get_student_average(6) == None
