import sys
from pathlib import Path

src_path = Path(__file__).resolve().parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
    
from models.AutomoveisList import AutomoveisList
from  views import view
def automovel_controller():
  automoveis_lista=AutomoveisList()
  while True:
    view.mostrar_menu()
    escolha = view.capturar_escolha()
    if escolha== '1':
      placa,modelo,marca,ano,valor =view.dados_automovel()
      automoveis_lista.adicionar_automovel(placa,modelo,marca,ano,valor)
    elif escolha=='2':
      placa=view.pedir_placa()
      automoveis_lista.deletar_automovel(placa)
    elif escolha=='3':
      placa,modelo,marca,ano,valor =view.dados_automovel()
      automoveis_lista.editar_automovel(placa,modelo,marca,ano,valor)
      
    elif escolha=='4':
      placa=view.pedir_placa()
      automovel = automoveis_lista.buscar_automovel(placa)
      if automovel:
        print(automovel.mostrar_automovel())
    elif escolha =='5':
      print('caiu aqui escolha==5')
      automoveis_lista.mostrar_todos_automoveis()
    
    elif escolha=='6':
      break
    else:
      print('Opção inválida !!')