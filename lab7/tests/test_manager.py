from __future__ import annotations

import datetime
import json

import pytest
from entities import Lab
from entities import Problem
from entities import Student
from repository import LabRepository
from repository import StudentRepository
from repository import SubmissionRepository
from services import LabService
from services import StudentService
from services import SubmissionService


@pytest.fixture
def sample_data() -> list:
    """Returns sample data for testing"""
    with open("data/sample.json") as f:
        return json.load(f)


@pytest.fixture
def services() -> tuple[LabService, StudentService, SubmissionService]:
    """Returns services for testing"""
    lab_repo = LabRepository()
    student_repo = StudentRepository()
    submission_repo = SubmissionRepository()

    lab_service = LabService(lab_repo)
    student_service = StudentService(student_repo)
    submission_service = SubmissionService(
        submission_repo,
        lab_service,
        student_service,
    )

    return (lab_service, student_service, submission_service)


def load_json(
    data,
    lab_service: LabService,
    student_service: StudentService,
    submission_service: SubmissionService,
):
    """Loads data from json"""
    lab_service.load_json(data["labs"])
    student_service.load_json(data["students"])
    submission_service.load_json(data["submissions"])


def test_load_json(sample_data, services):
    """
    +--------------------------+--------+
    |          Input           | Output |
    +--------------------------+--------+
    | manager.student_count    |      5 |
    | manager.lab_count        |      2 |
    | manager.submission_count |      6 |
    +--------------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert student_service.student_count == 5
    assert lab_service.lab_count == 2
    assert submission_service.submission_count == 6


def test_get_students(sample_data, services):
    """Returns a list of students
    +---------------------------+--------+
    |           Input           | Output |
    +---------------------------+--------+
    | len(manager.get_students) |      5 |
    +---------------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(student_service.get_students()) == 5


def test_get_student_by_id(sample_data, services):
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
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert student_service.get_student_by_id(1).name == "John"
    assert student_service.get_student_by_id(2).name == "Mary"
    assert student_service.get_student_by_id(3).name == "Peter"
    assert student_service.get_student_by_id(4).name == "Ann"
    assert student_service.get_student_by_id(5).name == "Bob"
    assert student_service.get_student_by_id(6) is None


def test_get_failing_students(sample_data, services):
    """
    +-------------------------------------+--------+
    |                Input                | Output |
    +-------------------------------------+--------+
    | len(manager.get_failing_students()) |      1 |
    +-------------------------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(submission_service.get_failing_students()) == 1
    assert submission_service.get_failing_students()[0][0].name == "Bob"


def test_search_student_by_group(sample_data, services):
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
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(student_service.search_student_by_group(311)) == 2
    assert len(student_service.search_student_by_group(312)) == 2
    assert len(student_service.search_student_by_group(313)) == 1
    assert len(student_service.search_student_by_group(314)) == 0


def test_search_student_by_name(sample_data, services):
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
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(student_service.search_student_by_name("John")) == 1
    assert len(student_service.search_student_by_name("Mary")) == 1
    assert len(student_service.search_student_by_name("Peter")) == 1
    assert len(student_service.search_student_by_name("Ann")) == 1
    assert len(student_service.search_student_by_name("Bob")) == 1
    assert len(student_service.search_student_by_name("Alice")) == 0


def test_add_student(sample_data, services):
    """
    +---------------------------+--------+
    |           Input           | Output |
    +---------------------------+--------+
    | get_student_by_id(6).name | "Alice"|
    +---------------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    student_service.add_student(Student(6, "Alice", 314))
    assert student_service.student_count == 6
    assert student_service.get_student_by_id(6).name == "Alice"
    with pytest.raises(ValueError):
        student_service.add_student(Student(6, "Alice", 314))


def test_delete_student_by_id(sample_data, services):
    """
    +----------------------+--------+
    |        Input         | Output |
    +----------------------+--------+
    | get_student_by_id(1) | None   |
    +----------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    student_service.delete_student_by_id(1)
    assert student_service.student_count == 4
    assert student_service.get_student_by_id(1) is None


def test_get_labs(sample_data, services):
    """
    +----------------------+--------+
    |        Input         | Output |
    +----------------------+--------+
    | len(manager.get_labs)|      2 |
    +----------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(lab_service.get_labs()) == 2


def test_get_lab_by_id(sample_data, services):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | get_lab_by_id(1) | not None |
    | get_lab_by_id(2) | not None |
    | get_lab_by_id(3) | None     |
    +------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert lab_service.get_lab_by_id(1) is not None
    assert lab_service.get_lab_by_id(2) is not None
    assert lab_service.get_lab_by_id(3) is None


def test_add_lab(sample_data, services):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | manager.lab_count|        3 |
    +------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    lab_service.add_lab(Lab(3))
    with pytest.raises(ValueError):
        lab_service.add_lab(Lab(3))
    assert lab_service.lab_count == 3


def test_delete_lab(sample_data, services):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | manager.lab_count|        1 |
    +------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    lab_service.delete_lab(lab_service.get_lab_by_id(1))
    assert lab_service.lab_count == 1
    assert lab_service.get_lab_by_id(1) is None


def test_delete_lab_by_id(sample_data, services):
    """
    +------------------+----------+
    |      Input       |  Output  |
    +------------------+----------+
    | manager.lab_count|        1 |
    +------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    lab_service.delete_lab_by_id(1)
    assert lab_service.lab_count == 1
    assert lab_service.get_lab_by_id(1) is None


def test_get_problems(sample_data, services):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | len(manager.get_problems)|        5 |
    +--------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(lab_service.get_problems()) == 5


def test_get_problem_by_ids(sample_data, services):
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
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert lab_service.get_problem_by_ids(1, 1).description == "Problem 1"
    assert lab_service.get_problem_by_ids(1, 2).description == "Problem 2"
    assert lab_service.get_problem_by_ids(1, 3).description == "Problem 3"
    assert lab_service.get_problem_by_ids(2, 1).description == "Problem 1"
    assert lab_service.get_problem_by_ids(2, 2).description == "Problem 2"
    assert lab_service.get_problem_by_ids(2, 3) is None
    assert lab_service.get_problem_by_ids(3, 1) is None


def test_add_problem(sample_data, services):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | manager.problem_count    |        6 |
    +--------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    lab_service.add_problem(1, Problem(4, "Problem 4", "2022-10-10"))
    problem = lab_service.get_problem_by_ids(1, 4)
    assert type(problem.deadline) is datetime.datetime
    assert lab_service.problem_count == 6
    with pytest.raises(ValueError):
        lab_service.add_problem(1, Problem(4, "Problem 4", "2022-10-10"))
    with pytest.raises(ValueError):
        lab_service.add_problem(3, Problem(4, "Problem 4", "2022-10-10"))


def test_search_problem_by_description(sample_data, services):
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
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(lab_service.search_problem_by_description("Problem 1")) == 2
    assert len(lab_service.search_problem_by_description("Problem 2")) == 2
    assert len(lab_service.search_problem_by_description("Problem 3")) == 1
    assert len(lab_service.search_problem_by_description("Problem 4")) == 0


def test_delete_problem_by_ids(sample_data, services):
    """
    +--------------------------+----------+
    |        Input             |  Output  |
    +--------------------------+----------+
    | manager.problem_count    |        4 |
    +--------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    lab_service.delete_problem_by_ids(1, 1)
    assert lab_service.get_problem_by_ids(1, 1) is None
    assert lab_service.problem_count == 4


def test_get_submissions(sample_data, services):
    """
    +-----------------------------+----------+
    |        Input                |  Output  |
    +-----------------------------+----------+
    | len(manager.get_submissions)|        6 |
    +-----------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(submission_service.get_submissions()) == 6


def test_get_lab_submissions(sample_data, services):
    """
    +--------------------------------------+----------+
    |        Input                         |  Output  |
    +--------------------------------------+----------+
    | len(manager.get_lab_submissions(1))  |        5 |
    | len(manager.get_lab_submissions(2))  |        1 |
    | len(manager.get_lab_submissions(3))  |        0 |
    +--------------------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert len(submission_service.get_lab_submissions(1)) == 5
    assert len(submission_service.get_lab_submissions(2)) == 1
    assert len(submission_service.get_lab_submissions(3)) == 0


def test_delete_submission(sample_data, services):
    """
    +-----------------------------+----------+
    |        Input                |  Output  |
    +-----------------------------+----------+
    | len(manager.get_submissions)|        5 |
    +-----------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    submission_service.delete_submission(1, 1, 1)
    assert len(submission_service.get_submissions()) == 5
    with pytest.raises(ValueError):
        submission_service.delete_submission(1, 1, 1)


def test_assign_lab_problem(sample_data, services):
    """
    +------------------------------------+----------+
    |        Input                       |  Output  |
    +------------------------------------+----------+
    | len(manager.get_lab_submissions(1))|        6 |
    +------------------------------------+----------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    submission_service.assign_lab_problem(4, 1, 1)
    assert len(submission_service.get_lab_submissions(1)) == 6
    with pytest.raises(ValueError):
        submission_service.assign_lab_problem(6, 1, 1)
    with pytest.raises(ValueError):
        submission_service.assign_lab_problem(1, 3, 1)
    with pytest.raises(ValueError):
        submission_service.assign_lab_problem(1, 1, 6)


def test_get_student_average(sample_data, services):
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
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert submission_service.get_student_average(1) == 10
    assert submission_service.get_student_average(2) == 9.5
    assert submission_service.get_student_average(3) is None
    assert submission_service.get_student_average(4) == 8
    assert submission_service.get_student_average(5) == 3.5
    assert submission_service.get_student_average(6) == None


def test_get_lab_grades_str(sample_data, services):
    """
    +----------------------------------+--------+
    |             Input                | Output |
    +----------------------------------+--------+
    | manager.get_lab_grades_string(1) | string |
    +----------------------------------+--------+
    """
    lab_service, student_service, submission_service = services
    load_json(sample_data, lab_service, student_service, submission_service)
    assert submission_service.get_lab_grades_str(1)
