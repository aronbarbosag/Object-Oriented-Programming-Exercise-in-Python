class Aluno:
    def __init__(self, matricula, nome, coeficiente_rendimento):
        self.matricula = matricula
        self.nome = nome
        self.coeficiente_rendimento = coeficiente_rendimento

    def __str__(self):
        return f"[{self.matricula}, {self.nome}, {self.coeficiente_rendimento}]"

    def __repr__(self):
        return f"Aluno({self.matricula}, {self.nome}, {self.coeficiente_rendimento})"
