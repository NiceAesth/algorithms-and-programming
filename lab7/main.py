from __future__ import annotations

import repository
import services
import ui


def main() -> None:
    """Main function. Runs a menu."""

    lab_repo = repository.LabFileRepository("data/labs.json")
    student_repo = repository.StudentFileRepository("data/students.json")
    submission_repo = repository.SubmissionFileRepository("data/submissions.json")

    lab_service = services.LabService(lab_repo)
    student_service = services.StudentService(student_repo)
    submission_service = services.SubmissionService(
        submission_repo,
        lab_service,
        student_service,
    )

    menu = ui.MainMenu(lab_service, student_service, submission_service)

    menu.run()


if __name__ == "__main__":
    main()
