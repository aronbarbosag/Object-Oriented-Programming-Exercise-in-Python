from src.controllers.create_student_controller import CreateStudentController
from src.models.repository.student_repository import student_repository
from src.views.create_student_view import CreateStudentView


def create_student_constructor():
    create_student_view = CreateStudentView()

    response = create_student_view.create()

    create_student_controller = CreateStudentController()
    status_response = create_student_controller.create(response)

    if status_response["success"]:
        student_repository.insert_student(status_response)
        create_student_view.create_student_success(status_response)

    else:
        create_student_view.create_student_fail(status_response)
