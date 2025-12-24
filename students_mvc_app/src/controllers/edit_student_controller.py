from src.models.entities.student import Aluno
from src.models.repository.student_repository import __StudentRepository


class EditStudentController:
    def edit(self, repo: __StudentRepository, student_id: int):
        try:
            self.__validate(repo, student_id)
            student = self.__search_student(repo, student_id)
            response = self.__format_response(student)

            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate(self, repo: __StudentRepository, student_id: int):
        if not student_id:
            raise Exception("Campo student id vazio !")

        if not isinstance(student_id, int):
            raise Exception("Campo id deve ser inteiro!!")

    def __search_student(self, repo: __StudentRepository, student_id: int):
        al = repo.search_student(student_id)
        if not al:
            return None

        return al

    def __format_response(self, student: Aluno):
        return {
            "Count": 1,
            "Attributes": {
                "matricula": student.matricula,
                "nome": student.nome,
                "CR": student.coeficiente_rendimento,
            },
        }
