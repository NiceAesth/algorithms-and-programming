from __future__ import annotations

from entities import Submission


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
