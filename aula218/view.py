from model import Carro


def menu():
    opcao = input(
        """
                  ----Menu----
                  (1) Cadastrar carros
                  (2) Mostrar carros
                  (3) Sair do programa
                  
                  """
    )
    return opcao


def entrada_dados_carro():
    carro = input("Digite o nome do carro: ")
    return carro


def entrada_dados_fabricante():
    fabricante = input("Digite o fabricante: ")
    return fabricante


def entrada_dados_motor_carro():
    motor = input("Digite o modelo do motor do carro: ")
    return motor


def entrada_criterio_ordenacao():
    criterio = input("Digite o criterio de ordenação: ").lower()
    return criterio
