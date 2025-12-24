class CreateStudentView:
    def create(self) -> dict:
        print("Cadastro de alunos\n\n")

        _id = input("Matricula: ")
        name = input("Nome: ")
        cr = input("Coeficiente de rendimento: ")

        response = {"matricula": _id, "nome": name, "CR": cr}

        return response

    def create_student_success(self, view_response: dict):
        message = view_response["message"]
        print("Aluno criado com sucesso!\n\n")
        print(message)

    def create_student_fail(self, view_response: dict):
        error = view_response["error"]
        print("Ocorreu um erro nessa transação!\n\n")
        print(error)
