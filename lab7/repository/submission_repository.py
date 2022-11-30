from __future__ import annotations

import dataclasses
import json

from entities import Submission
from helpers.data import DateTimeEncoder


class SubmissionRepository:
    """Submission repository"""

    def __init__(self) -> None:
        """Initialize the submission repository"""
        self.__submissions = []

    @property
    def submission_count(self) -> int:
        """Returns the number of submissions

        Returns:
            int: number of submissions
        """
        return len(self.__submissions)

    def load_json(self, obj: list) -> None:
        """Loads data from a JSON object

        Args:
            obj (list): list of data
        """
        self.__submissions.clear()
        for x in obj:
            self.__submissions.append(Submission.from_type(x))

    def get_submissions(self) -> list[Submission]:
        """Returns a list of all submissions

        Returns:
            list[Submission]: list of all submissions
        """
        return self.__submissions

    def add_submission(self, submission: Submission) -> None:
        """Adds a submission

        Args:
            submission (Submission): submission to add
        """
        self.__submissions.append(submission)

    def remove_submission(self, submission: Submission) -> None:
        """Removes a submission

        Args:
            submission (Submission): submission to remove
        """
        self.__submissions.remove(submission)


class SubmissionFileRepository(SubmissionRepository):
    """Submission file repository"""

    def __init__(self, filename: str) -> None:
        """Initialize the submission file repository

        Args:
            filename (str): name of the file
        """
        super().__init__()
        self.__filename = filename
        self.__load()

    def __load(self) -> None:
        """Loads data from the file"""
        try:
            with open(self.__filename) as f:
                self.load_json(json.load(f))
        except FileNotFoundError:
            pass

    def __save(self) -> None:
        """Saves data to the file"""
        with open(self.__filename, "w") as file:
            json.dump([dataclasses.asdict(x) for x in self.get_submissions()], file)

    def add_submission(self, submission: Submission) -> None:
        """Adds a submission

        Args:
            submission (Submission): submission to add
        """
        super().add_submission(submission)
        self.__save()

    def remove_submission(self, submission: Submission) -> None:
        """Removes a submission

        Args:
            submission (Submission): submission to remove
        """
        super().remove_submission(submission)
        self.__save()
