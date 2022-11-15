from __future__ import annotations

from .lab import Lab
from .student import Student
from .submission import Submission

__all__ = ["AppManager"]


class AppManager:
    def __init__(self) -> None:
        self.__students: list[Student] = []
        self.__labs: list[Lab] = []
        self.__submissions: list[Submission] = []

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

    def search_lab_by_description(self, description: str) -> list[Lab]:
        """Searches for labs with the given description

        Args:
            description (str): description of the lab

        Returns:
            labs (list[Lab]): list of labs with the given description
        """
        return [x for x in self.__labs if x.description == description]

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

    def get_submission(self, sid: int, lid: int) -> Submission | None:
        """Returns a submission with the given student and lab IDs

        Args:
            sid (int): ID of the student
            lid (int): ID of the lab

        Returns:
            submission (Submission): Submission with the given student and lab IDs
        """
        for submission in self.__submissions:
            if submission.sid == sid and submission.lid == lid:
                return submission
        return None

    def assign_lab(self, sid: int, lid: int, grade: float = None) -> Submission:
        """Assigns a lab to a student

        Args:
            sid (int): student ID
            lid (int): lab ID
            grade (float | None): grade (None if not submitted)

        Returns:
            Submission: the added submission
        """
        if submission := self.get_submission(sid, lid) is not None:
            self.__submissions.remove(submission)
        self.__submissions.append(Submission(sid, lid, grade))
        return self.__submissions[-1]
