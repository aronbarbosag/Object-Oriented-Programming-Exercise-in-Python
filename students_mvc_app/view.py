def mostrar_menu():
  print('1 - Adicionar aluno')
  print('2 - Listar alunos')
  print('3 - Alterar aluno')
  print('4 - Excluir aluno')
  print('0 - Sair')
  
def mostrar_alunos(alunos):
  for aluno in alunos:
    print(aluno.listar_aluno())
    
def pedir_dados_aluno():
  matricula = int(input('Matricula: '))
  nome = input('Nome: ')
  cr = input('Coeficiente de rendimento: ')
  return matricula,nome, cr

