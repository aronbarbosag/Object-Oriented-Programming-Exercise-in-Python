def menu():
    opcao = input(
        """
                  ----Menu----
                  (1) Cadastrar carros
                  (2) Mostrar carros
                  (3) Sair do programa
                  (4) Buscar carro
                  (5) Deletar carro
                  
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


def entrada_id_carro():
    id = int(input("Digite o id para buscar o carro: "))
    return id


def listar_carros(lista):
    if type(lista) == list:
        for carro in lista:
            print(carro.mostrar_caracteristicas_carro())
        return
    print(lista)


def delete_sucess(resultado):
    if resultado:
        print("Deleção feita com sucesso!")
    else:
        print("Falha em deletar o arquivo.")
