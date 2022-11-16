from __future__ import annotations

from statistics import mean
from statistics import StatisticsError

from .lab import Lab
from .lab import Problem
from .student import Student
from .submission import Submission

__all__ = ["AppManager"]


class AppManager:
    """Application data manager"""

    def __init__(self) -> None:
        """Initializes the manager"""
        self.__students: list[Student] = []
        self.__labs: list[Lab] = []
        self.__submissions: list[Submission] = []

    @property
    def student_count(self) -> int:
        """Returns the number of students

        Returns:
            int: number of students
        """
        return len(self.__students)

    @property
    def lab_count(self) -> int:
        """Returns the number of labs

        Returns:
            int: number of labs
        """
        return len(self.__labs)

    @property
    def submission_count(self) -> int:
        """Returns the number of submissions

        Returns:
            int: number of submissions
        """
        return len(self.__submissions)

    @property
    def problem_count(self) -> int:
        """Returns the number of problems

        Returns:
            int: number of problems
        """
        return len(self.get_problems())

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__students.clear()
        self.__labs.clear()
        self.__submissions.clear()
        for x in obj["students"]:
            self.__students.append(Student.from_type(x))
        for x in obj["labs"]:
            self.__labs.append(Lab.from_type(x))
        for x in obj["submissions"]:
            self.__submissions.append(Submission.from_type(x))

    def get_students(self) -> list[Student]:
        """Gets the list of all students

        Returns:
            list[Student]: list of students
        """
        return self.__students

    def get_student_by_id(self, sid: int) -> Student | None:
        """Returns a student with the given ID

        Args:
            sid (int): ID of the student

        Returns:
            student (Student): Student with the given ID
        """
        for student in self.__students:
            if student.sid == sid:
                return student
        return None

    def get_failing_students(self) -> list[tuple[Student, int]]:
        """Returns a tuple of students with failing grades and their grades

        Returns:
            list[tuple[Student, int]]: list of students with failing grades and their grades
        """
        res = []
        for x in self.__students:
            if (avg := self.get_student_average(x.sid)) is not None and avg < 5:
                res.append((x, avg))
        return res

    def search_student_by_group(self, group: int) -> list[Student]:
        """Returns a list of students in the given group

        Args:
            group (int): group number

        Returns:
            students (list[Student]): list of students in the given group
        """
        return [x for x in self.__students if x.group == group]

    def search_student_by_name(self, name: str) -> list[Student]:
        """Searches for students with the given name

        Args:
            name (str): name of the student

        Returns:
            students (list[Student]): list of students with the given name
        """
        return [x for x in self.__students if x.name == name]

    def add_student(self, obj: Student | dict) -> Student:
        """Adds a student to the list

        Args:
            obj (Student | dict): student data

        Returns:
            Student: the added student
        """
        student = Student.from_type(obj)
        if self.get_student_by_id(student.sid) is not None:
            raise ValueError("Student with the given ID already exists")
        self.__students.append(student)
        return self.__students[-1]

    def delete_student(self, obj: Student | dict) -> None:
        """Deletes a student from the list

        Args:
            obj (Student | dict): student data
        """
        self.__students.remove(Student.from_type(obj))

    def delete_student_by_id(self, sid: int) -> None:
        """Deletes a student from the list by ID

        Args:
            sid (int): student ID
        """
        self.__students.remove(self.get_student_by_id(sid))

    def get_labs(self) -> list[Lab]:
        """Gets the list of all labs

        Returns:
            list[Lab]: list of labs
        """
        return self.__labs

    def get_lab_by_id(self, lid: int) -> Lab | None:
        """Returns a lab with the given ID

        Args:
            lid (int): ID of the lab

        Returns:
            lab (Lab): Lab with the given ID
        """
        for lab in self.__labs:
            if lab.lid == lid:
                return lab
        return None

    def add_lab(self, obj: Lab | dict) -> Lab:
        """Adds a lab to the list

        Args:
            obj (Lab | dict): lab data

        Returns:
            Lab: the added lab
        """
        lab = Lab.from_type(obj)
        if self.get_lab_by_id(lab.lid) is not None:
            raise ValueError("Lab with the given ID already exists")
        self.__labs.append(lab)
        return self.__labs[-1]

    def delete_lab(self, obj: Lab | dict) -> None:
        """Deletes a lab from the list

        Args:
            obj (Lab | dict): lab data
        """
        self.__labs.remove(Lab.from_type(obj))

    def delete_lab_by_id(self, lid: int) -> None:
        """Deletes a lab from the list by ID

        Args:
            lid (int): lab ID
        """
        self.__labs.remove(self.get_lab_by_id(lid))

    def get_problems(self) -> list[Problem]:
        """Gets the list of all problems

        Returns:
            list[Problem]: list of problems
        """
        return [x for lab in self.__labs for x in lab.problems]

    def get_problem_by_ids(self, lid: int, pid: int) -> Problem | None:
        """Returns a submission with the given ID

        Args:
            lid (int): ID of the lab
            pid (int): ID of the problem

        Returns:
            submission (Submission): Submission with the given ID
        """
        for lab in self.__labs:
            if lab.lid == lid:
                for problem in lab.problems:
                    if problem.pid == pid:
                        return problem
        return None

    def add_problem(self, lid: int, obj: Problem | dict) -> Problem:
        """Adds a problem to the list

        Args:
            lid (int): ID of the lab
            obj (Problem | dict): problem data

        Returns:
            Problem: the added problem
        """
        problem = Problem.from_type(obj)
        lab = self.get_lab_by_id(lid)
        if lab is None:
            raise ValueError("Lab with the given ID does not exist")
        if self.get_problem_by_ids(lid, problem.pid) is not None:
            raise ValueError("Problem with the given ID already exists")
        lab.problems.append(problem)
        return lab.problems[-1]

    def search_problem_by_description(self, description: str) -> list[Problem]:
        """Searches for problems with the given description

        Args:
            description (str): description of the problem

        Returns:
            problems (list[Problem]): list of problems with the given description
        """
        return [x for x in self.get_problems() if x.description == description]

    def delete_problem_by_ids(self, lid: int, pid: int) -> None:
        """Deletes a problem from the list by IDs

        Args:
            lid (int): lab ID
            pid (int): problem ID
        """
        for lab in self.__labs:
            if lab.lid == lid:
                lab.problems.remove(self.get_problem_by_ids(lid, pid))

    def get_submission(self, sid: int, lid: int, pid: int) -> Submission | None:
        """Returns a submission with the given student and lab IDs

        Args:
            sid (int): ID of the student
            lid (int): ID of the lab
            pid (int): ID of the problem

        Returns:
            submission (Submission): Submission with the given student and lab IDs
        """
        for submission in self.__submissions:
            if (
                submission.sid == sid
                and submission.lid == lid
                and submission.pid == pid
            ):
                return submission
        return None

    def get_submissions(self) -> list[Submission]:
        """Gets the list of all submissions

        Returns:
            list[Submission]: list of submissions
        """
        return self.__submissions

    def get_lab_submissions(self, lid: int) -> list[Submission]:
        """Returns a list of submissions for the given lab

        Args:
            lid (int): ID of the lab

        Returns:
            submissions (list[Submission]): list of submissions for the given lab
        """
        return [x for x in self.__submissions if x.lid == lid]

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
        if self.get_student_by_id(sid) is None:
            raise ValueError("Student with the given ID does not exist")
        if self.get_lab_by_id(lid) is None:
            raise ValueError("Lab with the given ID does not exist")
        if self.get_problem_by_ids(lid, pid) is None:
            raise ValueError("Problem with the given ID does not exist")
        if (submission := self.get_submission(sid, lid, pid)) is not None:
            self.__submissions.remove(submission)

        self.__submissions.append(Submission(sid, lid, pid, grade))
        return self.__submissions[-1]

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
                    for x in self.__submissions
                    if x.sid == sid and x.grade is not None
                ],
            )
        except StatisticsError:
            return None

    def __get_student_submission_pairs(self) -> list[tuple[Student, Submission]]:
        """Returns a list of tuples of students and their submissions

        Returns:
            list[tuple[Student, Submission]]: list of tuples of students and their submissions
        """
        return [
            (self.get_student_by_id(x.sid), x)
            for x in self.__submissions
            if x.grade is not None
        ]

    def get_lab_grades_str(self, lid: int) -> str:
        """Returns a string with the grades of a lab

        Args:
            lid (int): lab ID

        Returns:
            grades (str): string with the grades of a lab
        """
        lab = self.get_lab_by_id(lid)
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
