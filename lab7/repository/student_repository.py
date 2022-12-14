from __future__ import annotations

import dataclasses
import json

from entities import Student


class StudentRepository:
    """Student repository class."""

    def __init__(self):
        """Initialize the student repository."""
        self.__students = []

    @property
    def student_count(self) -> int:
        """Returns the number of students

        Returns:
            int: number of students
        """
        return len(self.__students)

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__students.clear()
        for x in obj:
            self.__students.append(Student.from_type(x))

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


class StudentFileRepository(StudentRepository):
    """Student file repository class."""

    def __init__(self, filename: str):
        """Initialize the student file repository.

        Args:
            filename (str): name of the file
        """
        super().__init__()
        self.__filename = filename
        self.load()

    def load(self) -> None:
        """Loads data from the file."""
        with open(self.__filename) as file:
            self.load_json(json.load(file))

    def save(self) -> None:
        """Saves data to the file."""
        with open(self.__filename, "w") as file:
            json.dump([dataclasses.asdict(x) for x in self.get_students()], file)

    def add_student(self, obj: Student | dict) -> Student:
        """Adds a student to the list

        Args:
            obj (Student | dict): student data

        Returns:
            Student: the added student
        """
        student = super().add_student(obj)
        self.save()
        return student

    def delete_student(self, obj: Student | dict) -> None:
        """Deletes a student from the list

        Args:
            obj (Student | dict): student data
        """
        super().delete_student(obj)
        self.save()
