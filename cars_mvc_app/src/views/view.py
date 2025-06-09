def mostrar_menu():
  print(""" <<-- Escolha uma opção -->>
        (1) Inserir um novo automóvel
        (2) Excluir um automóvel
        (3) Alterar um automóvel
        (4) Consultar um automóvel
        (5) Mostrar todos os automóveis
        (6) Sair 
        """)
  
def capturar_escolha():
  escolha = input(' ').strip()
  return escolha

def dados_automovel():
  placa = input('Placa: ').strip()
  modelo = input('Modelo: ').strip()
  marca = input('Marca: ').strip()
  while True:
    try:
      ano = int(input('Ano: '))
      break
    except ValueError:
      print('Ano deve ser um número inteiro.')
  while True:
    try:    
      valor = float(input('Valor: '))
      break
    except ValueError:
      print('Valor deve ser um numéro real')
  
  return placa,modelo,marca,ano,valor
 
def pedir_placa():
    placa = input('Placa: ').strip()
    return placa