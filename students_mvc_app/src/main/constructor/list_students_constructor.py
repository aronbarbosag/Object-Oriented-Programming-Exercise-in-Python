from src.models.repository.student_repository import student_repository
from src.views.list_students_view import ListStudentView


def list_students_constructor():
    create_student_view = ListStudentView()

    students_list = student_repository.list_all_students()

    create_student_view.list(students_list)
