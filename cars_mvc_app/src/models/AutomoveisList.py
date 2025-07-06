from models.Automovel import Automovel
import pathlib


class AutomoveisList:

    def __init__(self):
        self.automoveis_lista = []

    def adicionar_automovel(self, placa, modelo, marca, ano, valor):
        if self.buscar_automovel(placa) is None:
            automovel = Automovel(placa, modelo, marca, ano, valor)
            self.automoveis_lista.append(automovel)
            self.salvar_dados()
        else:
            print(f"A placa {automovel.placa} já existe.")

    def deletar_automovel(self, placa):
        if self.buscar_automovel(placa):
            automovel = self.buscar_automovel(placa)
            self.automoveis_lista.remove(automovel)
            self.salvar_dados()
        else:
            print(f"Automovel com a placa {placa} não foi encontrado.")

    def editar_automovel(self, placa, modelo, marca, ano, valor):
        if self.buscar_automovel(placa):
            automovel = self.buscar_automovel(placa)
            automovel.set_modelo(modelo)
            automovel.set_marca(marca)
            automovel.set_ano(ano)
            automovel.set_valor(valor)
            self.salvar_dados()

    def mostrar_todos_automoveis(self):
        self.carregar_dados()
        for a in self.automoveis_lista:
            print(a.mostrar_automovel())

    def buscar_automovel(self, placa):
        for automovel in self.automoveis_lista:
            if automovel.placa == placa:
                return automovel
        return None

    def salvar_dados(self):
        caminho_arquivo = pathlib.Path(__file__).resolve().parent.parent / "database"
        caminho_arquivo.mkdir(exist_ok=True)
        with open(caminho_arquivo / "automoveis.txt", "w") as file:
            for automovel in self.automoveis_lista:
                linha = f"{automovel.get_placa()},{automovel.get_modelo()},{automovel.get_marca()}, {automovel.get_ano()},{automovel.get_valor()}\n"
                file.write(linha)

    def carregar_dados(self):
        caminho_arquivo = pathlib.Path(__file__).resolve().parent.parent / "database"
        caminho_arquivo.mkdir(exist_ok=True)
        arquivo_automoveis = caminho_arquivo / "automoveis.txt"

        if not arquivo_automoveis.exists():
            arquivo_automoveis.touch()
            return

        with open(arquivo_automoveis, "r") as file:
            for row in file:
                linha = row.strip().split(",")
                placa = linha[0]
                modelo = linha[1]
                marca = linha[2]
                ano = int(linha[3])
                valor = float(linha[4])
                if self.buscar_automovel(placa) is None:
                    automovel = Automovel(placa, modelo, marca, ano, valor)
                    self.automoveis_lista.append(automovel)
