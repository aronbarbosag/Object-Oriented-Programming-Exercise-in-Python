from src.controllers.edit_student_controller import EditStudentController
from src.models.repository.student_repository import student_repository
from src.views.edit_student_view import EditStudentView


def edit_student_constructor():
    edit_student_view = EditStudentView()

    student_id = edit_student_view.edit()

    option = edit_student_view.edit_options()
    if option == "1":
        new_name = edit_student_view.name_edit()
        student_repository.edit_name(student_id, new_name)
    elif option == "2":
        new_cr = edit_student_view.cr_edit()
        student_repository.edit_cr(student_id, new_cr)

    else:
        print("Opção não encontrada!")

    response = edit_student_controller = EditStudentController().edit(
        student_repository, student_id
    )

    if response["success"]:
        edit_student_view.success_edit(response["message"])
    else:
        edit_student_view.fail_edit(response["error"])
