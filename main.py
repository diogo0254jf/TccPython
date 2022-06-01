'''
Funcionario = {
Salário líquido = (Salário Bruto * 0.84) * 1.3
	ID, 
	Nome, 
	Matricula, 
	Cargo, 
	Departamento, 
	Salário
}
'''
class Funcionario:
    def __init__(self, ID, Nome, Matricula, Cargo, Departamento, Salario: float):
        self.ID = ID
        self.Nome = Nome
        self.Matricula = Matricula
        self.Cargo = Cargo
        self.Departamento = Departamento
        self.Salario = Salario
    
    def contratar(self,ID, Nome, Matricula, Cargo, Departamento, Salario: float):
        arquivo = open("funcionarios.txt", "r")
        arquivo.write(f"ID: {self.ID}\nNome: {self.Nome}\nMatricula: {self.Matricula}\nCargo: {self.Cargo}\nDepartamento: {self.Departamento}\nSalario: {self.Salario}\n") 
        print("Funcionario Contratado") 
'''
Departamento = {
 	ID,
 	Nome e Gerente
}
'''
class Departamento(Funcionario):
    def __init__(self, Departamento, ID, Nome, Gerente):
        self.Departamento = Departamento
        self.ID = ID
        self.Nome = Nome
        self.Gerente = Gerente
    
'''
Gerente = {
 	ID, 
 	Nome, 
 	Matricula, 
 	Cargo, 
 	Departamento, 
 	Salário
 	Setor
}
'''
class Gerente(Funcionario):
    def __init__(self, Salario: float,Departamento):
        self.Departamento = Departamento
        self.Salario = (Salario * 0.84) + (Salario * 0.5)
    

class Modo_de_Acesso:
    def __init__(self, modoAcesso):
        self.modoAcesso = modoAcesso
    pass

NewContact = Funcionario(1, "João", "123", "Programador", "TI", "1000")

NewContact.contratar()