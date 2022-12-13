from __future__ import annotations

import datetime

from entities import Lab
from entities import Problem
from entities import Student
from entities import Submission


def test_problem_from_type():
    problem = Problem.from_type(
        {
            "pid": 1,
            "description": "description",
            "deadline": datetime.datetime(year=2021, month=1, day=1),
        },
    )
    assert problem.pid == 1
    assert problem.description == "description"
    assert problem.deadline == datetime.datetime(year=2021, month=1, day=1)
    problem_new = Problem.from_type(problem)
    assert problem_new == problem


def test_problem_str():
    problem = Problem(1, "description", datetime.datetime(year=2021, month=1, day=1))
    assert str(problem)


def test_lab_from_type():
    lab = Lab.from_type({"lid": 1})
    assert lab.lid == 1
    lab_new = Lab.from_type(lab)
    assert lab_new == lab


def test_lab_str():
    lab = Lab(1)
    assert str(lab)


def test_lab_get_problem_by_id():
    lab = Lab(1)
    problem = Problem(1, "description", datetime.datetime(year=2021, month=1, day=1))
    lab.problems.append(problem)
    assert lab.get_problem_by_id(1) == problem
    assert lab.get_problem_by_id(2) is None


def test_student_from_type():
    student = Student.from_type({"sid": 1, "name": "name", "group": 1})
    assert student.sid == 1
    assert student.name == "name"
    student_new = Student.from_type(student)
    assert student_new == student


def test_student_str():
    student = Student(1, "name", 1)
    assert str(student)


def test_submission_from_type():
    submission = Submission.from_type(
        {
            "sid": 1,
            "lid": 1,
            "pid": 1,
            "grade": 10,
        },
    )
    assert submission.sid == 1
    assert submission.lid == 1
    assert submission.pid == 1
    assert submission.grade == 10
    submission_new = Submission.from_type(submission)
    assert submission_new == submission
