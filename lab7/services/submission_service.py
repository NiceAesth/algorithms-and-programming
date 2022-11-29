from __future__ import annotations

from statistics import mean
from statistics import StatisticsError

from entities import Student
from entities import Submission
from repository import SubmissionRepository
from services import LabService
from services import StudentService


class SubmissionService:
    def __init__(
        self,
        submission_repository: SubmissionRepository,
        lab_service: LabService,
        student_service: StudentService,
    ) -> None:
        """Initialize the submission service."""
        self.__repository = submission_repository
        self.lab_service = lab_service
        self.student_service = student_service

    @property
    def submission_count(self) -> int:
        """Returns the number of submissions

        Returns:
            int: number of submissions
        """
        return len(self.__repository.get_submissions())

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__repository.load_json(obj)

    def get_submissions(self) -> list[Submission]:
        """Returns a list of all submissions

        Returns:
            list[Submission]: list of all submissions
        """
        return self.__repository.get_submissions()

    def remove_submission(self, sid: int, lid: int, pid: int) -> None:
        """Removes a submission

        Args:
            sid (int): student ID
            lid (int): lab ID
            pid (int): problem ID
        """
        submission = self.get_submission(sid, lid, pid)
        if submission is None:
            raise ValueError("Submission does not exist")
        self.__repository.remove_submission(submission)

    def add_submission(self, submission: Submission) -> None:
        """Adds a submission

        Args:
            submission (Submission): submission to add
        """
        self.__repository.add_submission(submission)

    def get_submission(self, sid: int, lid: int, pid: int) -> Submission | None:
        """Returns a submission with the given student and lab IDs

        Args:
            sid (int): ID of the student
            lid (int): ID of the lab
            pid (int): ID of the problem

        Returns:
            submission (Submission): Submission with the given student and lab IDs
        """
        for submission in self.get_submissions():
            if (
                submission.sid == sid
                and submission.lid == lid
                and submission.pid == pid
            ):
                return submission
        return None

    def assign_lab_problem(
        self,
        sid: int,
        lid: int,
        pid: int,
        grade: float = None,
    ) -> Submission:
        """Assigns a lab to a student

        Args:
            sid (int): student ID
            lid (int): lab ID
            pid (int): problem ID
            grade (float | None): grade (None if not submitted)

        Returns:
            Submission: the added submission
        """
        if self.student_service.get_student_by_id(sid) is None:
            raise ValueError("Student with the given ID does not exist")
        if self.lab_service.get_lab_by_id(lid) is None:
            raise ValueError("Lab with the given ID does not exist")
        if self.lab_service.get_problem_by_ids(lid, pid) is None:
            raise ValueError("Problem with the given ID does not exist")
        try:
            self.remove_submission(sid, lid, pid)
        except ValueError:
            pass

        self.add_submission(Submission(sid, lid, pid, grade))
        return self.get_submissions()[-1]

    def __get_student_submission_pairs(self) -> list[tuple[Student, Submission]]:
        """Returns a list of tuples of students and their submissions

        Returns:
            list[tuple[Student, Submission]]: list of tuples of students and their submissions
        """
        return [
            (self.student_service.get_student_by_id(x.sid), x)
            for x in self.get_submissions()
            if x.grade is not None
        ]

    def get_lab_submissions(self, lid: int) -> list[Submission]:
        """Returns a list of submissions for the given lab

        Args:
            lid (int): ID of the lab

        Returns:
            submissions (list[Submission]): list of submissions for the given lab
        """
        return [x for x in self.get_submissions() if x.lid == lid]

    def get_lab_grades_str(self, lid: int) -> str:
        """Returns a string with the grades of a lab

        Args:
            lid (int): lab ID

        Returns:
            grades (str): string with the grades of a lab
        """
        lab = self.lab_service.get_lab_by_id(lid)
        res = [f"Lab {lab.lid}"]
        for x in sorted(
            self.__get_student_submission_pairs(),
            key=lambda x: (x[0].name, x[1].grade),
        ):
            student, submission = x
            if submission.lid == lid:
                problem = lab.get_problem_by_id(submission.pid)
                res.append(
                    f"{student.name} - {problem.description}, {submission.grade}",
                )
        return "\n".join(res)

    def get_student_average(self, sid: int) -> float:
        """Returns the average grade of a student

        Args:
            sid (int): student ID

        Returns:
            average (float): average grade
        """
        try:
            return mean(
                [
                    x.grade
                    for x in self.__repository.get_submissions()
                    if x.sid == sid and x.grade is not None
                ],
            )
        except StatisticsError:
            return None

    def get_failing_students(self) -> list[tuple[Student, int]]:
        """Returns a tuple of students with failing grades and their grades

        Returns:
            list[tuple[Student, int]]: list of students with failing grades and their grades
        """
        res = []
        for x in self.student_service.get_students():
            if (avg := self.get_student_average(x.sid)) is not None and avg < 5:
                res.append((x, avg))
        return res
