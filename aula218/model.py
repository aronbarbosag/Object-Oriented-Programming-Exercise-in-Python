class Carro:
    _proximo_id = 0

    def __init__(self, nome: str) -> None:
        self.id = Carro._proximo_id
        Carro._proximo_id += 1
        self.nome = nome
        self.motor = None
        self.fabricante = None

    def cadastrar_motor(self, nome: str) -> None:
        self.motor = Motor(nome)

    def cadastrar_fabricante(self, fabricante: "Fabricante") -> None:
        self.fabricante = fabricante

    def mostrar_caracteristicas_carro(self):
        return f"ID: {self.id} Fabricante: {self.fabricante} Carro: {self.nome} Motor: {self.motor}"


class Motor:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __str__(self):
        return self.nome


class Fabricante:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __str__(self):
        return self.nome
