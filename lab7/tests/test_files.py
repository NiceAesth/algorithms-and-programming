from __future__ import annotations

from repository import LabFileRepository
from repository import StudentFileRepository
from repository import SubmissionFileRepository


def test_lab_file_repository(mocker):
    mock_file = mocker.mock_open(read_data="[]")
    mocker.patch("builtins.open", mock_file)
    repo = LabFileRepository("test.json")
    assert repo.lab_count == 0
    repo.add_lab({"lid": 1, "problems": []})
    assert repo.lab_count == 1
    repo.add_problem(1, {"pid": 1, "description": "test", "deadline": "2021-01-01"})
    assert repo.problem_count == 1
    repo.delete_problem_by_ids(1, 1)
    assert repo.problem_count == 0
    repo.delete_lab({"lid": 1, "problems": []})
    assert repo.lab_count == 0


def test_student_file_repository(mocker):
    mock_file = mocker.mock_open(read_data="[]")
    mocker.patch("builtins.open", mock_file)
    repo = StudentFileRepository("test.json")
    assert repo.student_count == 0
    repo.add_student({"sid": 1, "name": "test", "group": 1})
    assert repo.student_count == 1
    repo.delete_student({"sid": 1, "name": "test", "group": 1})
    assert repo.student_count == 0


def test_submission_file_repository(mocker):
    mock_file = mocker.mock_open(read_data="[]")
    mocker.patch("builtins.open", mock_file)
    repo = SubmissionFileRepository("test.json")
    assert repo.submission_count == 0
    repo.add_submission({"sid": 1, "lid": 1, "pid": 1, "grade": 10})
    assert repo.submission_count == 1
    repo.delete_submission({"sid": 1, "lid": 1, "pid": 1, "grade": 10})
    assert repo.submission_count == 0
