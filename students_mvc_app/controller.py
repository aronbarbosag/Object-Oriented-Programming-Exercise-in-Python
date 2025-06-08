from model import AlunoArrayList
import view

def main():
  alunos = AlunoArrayList()
  while True:
    view.mostrar_menu()
    opcao = input('Escolha uma opção: ')
    if opcao == "1":
      matricula,nome,cr = view.pedir_dados_aluno()
      alunos.adicionar_aluno(matricula,nome,cr)
    elif opcao == '2':
      alunos.carregar_alunos()
      view.mostrar_alunos(alunos.alunosLista)
    elif opcao == '3':
      matricula = int(input('Matricula do aluno a alterar: '))
      nome = input('Novo nome: ')
      cr = input('Novo coeficiente de rendimento: ')
      alunos.alterar_aluno(matricula,nome,cr)
    elif opcao =='4':
      matricula = int(input('matricula do aluno a excluir: '))
      alunos.excluir_aluno(matricula)
    elif opcao == '0':
      break
    else:
      print('Opção inválida.')