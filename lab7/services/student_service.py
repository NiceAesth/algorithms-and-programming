from __future__ import annotations

from entities import Student
from repository import StudentRepository


class StudentService:
    """Student service class."""

    def __init__(self, student_repository: StudentRepository) -> None:
        """Initialize the student service."""
        self.__repository = student_repository

    @property
    def student_count(self) -> int:
        """Returns the number of students

        Returns:
            int: number of students
        """
        return self.__repository.student_count

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__repository.load_json(obj)

    def get_students(self) -> list[Student]:
        """Returns a list of all students

        Returns:
            list[Student]: list of all students
        """
        return self.__repository.get_students()

    def get_student_by_id(self, sid: int) -> Student | None:
        """Returns a student with the given ID

        Args:
            sid (int): ID of the student

        Returns:
            student (Student): Student with the given ID
        """
        for student in self.__repository.get_students():
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
        return [x for x in self.get_students() if x.group == group]

    def search_student_by_name(self, name: str) -> list[Student]:
        """Searches for students with the given name

        Args:
            name (str): name of the student

        Returns:
            students (list[Student]): list of students with the given name
        """
        return [x for x in self.get_students() if x.name == name]

    def add_student(self, obj: Student | dict) -> Student:
        """Adds a student to the list

        Args:
            obj (Student | dict): student data

        Returns:
            Student: the added student
        """
        self.__repository.add_student(obj)

    def delete_student_by_id(self, sid: int) -> None:
        """Deletes a student from the list by ID

        Args:
            sid (int): student ID
        """
        self.__repository.delete_student(self.get_student_by_id(sid))
