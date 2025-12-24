class EditStudentView:
    def edit(self) -> int:
        message = """
            Painel de Edição

            Digite a matricula do aluno
            para editar alguma informação.

        """
        print(message)
        matricula = int(input(""))
        return matricula

    def edit_options(self):
        message = """
            Qual campo você deseja editar ?

            (1) Nome
            (2) CR


        """
        print(message)

        command = input("")
        return command

    def name_edit(self) -> str:
        message = """
            Edição do nome selecionado!
        """
        print(message)
        name = input("")
        return name

    def cr_edit(self) -> int:
        message = """
            Edição do CR selecionada!
        """
        print(message)
        cr = float(input(""))
        return cr

    def success_edit(self, response: dict):
        print("\nEdição realizada com sucesso!\n")

        print(response)

    def fail_edit(self, response: dict):
        print("\nFalha na alteração dos dados!\n")

        print(response)
