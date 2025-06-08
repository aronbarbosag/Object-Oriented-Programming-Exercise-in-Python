class Aluno:
  def __init__(self,matricula,nome,coeficiente_rendimento):
    self.matricula = matricula
    self.nome = nome
    self.coeficiente_rendimento = coeficiente_rendimento
    
  def getMatricula(self):
    return self.matricula
  
  def getNome(self):
    return self.nome
  
  def getCoeficiente_rendimento(self):
    return self.coeficiente_rendimento
  
  def setNome(self,nome):
    self.nome = nome
    
  def setCR(self,cr):
    self.coeficiente_rendimento = cr
    
  def listar_aluno(self):
    return (f'Matricula:  {self.getMatricula()}   Nome:  {self.getNome()} CR:  {self.getCoeficiente_rendimento()}')
    

import os

class AlunoArrayList:
  
  def __init__(self):
    self.alunosLista = []
    self.carregar_alunos()
    
    
  
  
  
  def adicionar_aluno(self,matricula,nome,coeficiente_rendimento):
    if self.buscar_aluno(matricula) is None:
            al = Aluno(matricula, nome, coeficiente_rendimento)
            self.alunosLista.append(al)
            self.salvar_aluno()
    else:
            print("Aluno com essa matrícula já existe.")
    
  
  def buscar_aluno(self,matricula):
    for aluno in self.alunosLista:
      if aluno.matricula == matricula:
          return aluno
    return None
  
  def alterar_aluno(self,matricula,nome,coeficiente_rendimento):
    try:
      aluno = self.buscar_aluno(matricula)
      if aluno:
        aluno.setNome(nome)
        aluno.setCR(coeficiente_rendimento)
        self.salvar_aluno()
        print('alteração feita com sucesso!')
    except ValueError:
      print('Não existe nenhum aluno com essa matricula!')
   
  def salvar_aluno(self):
    with open('alunos.txt','w') as f:
      for aluno in self.alunosLista:
        f.write(f"{aluno.getMatricula()},{aluno.getNome()},{aluno.getCoeficiente_rendimento()}\n")
    pass    
         
      
      
  def excluir_aluno(self,matricula):
    aluno = self.buscar_aluno(matricula)
    if aluno:
         self.alunosLista.remove(aluno)
         self.salvar_aluno()
    else:
      print('Não existe nenhum aluno com essa matricula!')
   
      
      
   
    
  def listar_alunos(self):
    self.alunosLista = []
    self.carregar_alunos()
    for aluno in self.alunosLista:
      print(aluno.listar_aluno())
      
  def carregar_alunos(self):
    if not os.path.exists('alunos.txt'):
            open('alunos.txt', 'w').close()
    with open('alunos.txt','r') as f:
      for linha in f:
        if linha.strip():
          al = linha.strip().split(',')
          matricula = int(al[0])
          nome = al[1]
          co_rendimento = al[2]
          if self.buscar_aluno(matricula) is None:
            aluno = Aluno(matricula,nome,co_rendimento)
            self.alunosLista.append(aluno)
        
    pass