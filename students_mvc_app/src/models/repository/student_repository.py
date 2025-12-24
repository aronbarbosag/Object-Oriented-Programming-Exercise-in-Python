from src.models.entities.student import Aluno


class __StudentRepository:
    def __init__(self):
        self.students = []

    def insert_student(self, user_data: dict):
        message_data = user_data["message"]["Attributes"]
        _id = message_data["id"]
        name = message_data["name"]
        cr = message_data["cr"]

        if self.search_student(_id):
            raise Exception("Ja existe um aluno com esse id!")

        al = Aluno(_id, name, cr)

        self.students.append(al)

    def search_student(self, _id):
        for al in self.students:
            if al.matricula == _id:
                return al
        return None

    def list_all_students(self) -> list:
        return self.students


student_repository = __StudentRepository()
