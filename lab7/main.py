from __future__ import annotations

import repository
import services
import ui


def main() -> None:
    """Main function. Runs a menu."""
    lab_repo = repository.LabRepository()
    student_repo = repository.StudentRepository()
    submission_repo = repository.SubmissionRepository()
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
