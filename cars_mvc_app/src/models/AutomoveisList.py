from models.Automovel import Automovel

class AutomoveisList:
  
  def __init__(self):
    self.automoveis_lista = []
    
  def adicionar_automovel(self,placa, modelo, marca, ano, valor):
    if self.buscar_automovel(placa) is None:
      automovel = Automovel(placa,modelo, marca, ano,valor)
      self.automoveis_lista.append(automovel)
    else:
      print(f'A placa {automovel.placa} já existe.')
  
  def deletar_automovel(self,placa):
    if self.buscar_automovel(placa):
      automovel = self.buscar_automovel(placa)
      self.automoveis_lista.remove(automovel)
    else:
      print(f'Automovel com a placa {placa} não foi encontrado.')
  
  def editar_automovel(self,placa,modelo,marca,ano,valor):
    if self.buscar_automovel(placa):
      automovel = self.buscar_automovel(placa)
      automovel.set_modelo(modelo) 
      automovel.set_marca(marca) 
      automovel.set_ano(ano) 
      automovel.set_valor(valor)   
      
  def mostrar_todos_automoveis(self):
    for a in self.automoveis_lista:
        print(a.mostrar_automovel())
  
  def buscar_automovel(self,placa):
    for automovel in self.automoveis_lista:
      if automovel.placa ==placa:
        return automovel
    return None
  
  