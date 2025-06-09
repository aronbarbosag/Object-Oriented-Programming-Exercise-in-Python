class Automovel:
  
  def __init__(self,placa,modelo,marca,ano,valor):
    self.placa,self.modelo,self.marca,self.ano,self.valor = placa,modelo,marca,ano,valor
  
  def get_placa(self):
    return self.placa
  
  def set_placa(self,placa):
    self.placa = placa
  
  def get_modelo(self):
    return self.modelo
  
  def set_modelo(self,modelo):
    self.modelo = modelo
  
  def get_marca(self):
    return self.marca
  
  def set_marca(self,marca):
    self.marca = marca
  
  def get_ano(self):
    return self.ano
  
  def set_ano(self,ano):
    self.ano = ano
  
  def get_valor(self):
    return self.valor
  
  def set_valor(self,valor):
    self.valor = valor
    
  def mostrar_automovel(self):
   
    return (f'Placa: {self.get_placa()} Modelo: {self.get_modelo()} Marca: {self.get_marca()} Ano: {self.get_ano()} Valor: {self.get_valor()}')
    