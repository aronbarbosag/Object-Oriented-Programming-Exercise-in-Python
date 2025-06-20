from model import Carro, Fabricante
import view


def ordenar_lista_fabricante(lista_de_objetos, criterio="id"):
    criterios = {
        "fabricante": sorted(lista_de_objetos, key=lambda obj: obj.fabricante.nome),
        "nome": sorted(lista_de_objetos, key=lambda obj: obj.nome),
        "motor": sorted(lista_de_objetos, key=lambda obj: obj.motor.nome),
        "id": sorted(lista_de_objetos, key=lambda obj: obj.id),
    }
    return criterios[criterio]


def buscar_carro(lista_de_objetos, id: int):
    for objeto in lista_de_objetos:
        if objeto.id == id:
            return objeto
    return None


def deletar_carro(lista_de_objetos, id):
    if buscar_carro(lista_de_objetos, id):
        carro = buscar_carro(lista_de_objetos, id)
        lista_de_objetos.remove(carro)
        return True
    return False


def controller():
    lista_carros = []
    new_lista_carros = []
    while True:
        opcao = view.menu()
        if opcao.lower() == "3":
            break
        elif opcao.lower() == "1":
            carro_entrada = view.entrada_dados_carro()
            carro = Carro(carro_entrada)
            motor_entrada = view.entrada_dados_motor_carro()
            carro.cadastrar_motor(motor_entrada)
            fabricante_entrada = view.entrada_dados_fabricante()
            fabricante = Fabricante(fabricante_entrada)
            carro.cadastrar_fabricante(fabricante)
            lista_carros.append(carro)
        elif opcao.lower() == "2":
            criterio = view.entrada_criterio_ordenacao()
            new_lista_carros = ordenar_lista_fabricante(lista_carros, criterio)
            view.listar_carros(new_lista_carros)
        elif opcao.lower() == "4":
            id = view.entrada_id_carro()
            carro_achado = buscar_carro(
                lista_carros, id
            ).mostrar_caracteristicas_carro()
            view.listar_carros(carro_achado)
        elif opcao.lower() == "5":
            id = view.entrada_id_carro()
            resultado = deletar_carro(lista_carros, id)
            view.delete_sucess(resultado)
