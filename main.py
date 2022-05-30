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
    def __init__(self, ID, Nome, Matricula, Cargo, Departamento, Salario):
        self.ID = ID
        self.Nome = Nome
        self.Matricula = Matricula
        self.Cargo = Cargo
        self.Departamento = Departamento
        self.Salario = (Salario * 0.84) + (Salario * 1.3)
    pass
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
    pass
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
    def __init__(self, Salario,Departamento):
        self.Departamento = Departamento
        self.Salario = (Salario * 0.84) + (Salario * 0.5)
    pass

class Disco:
    def __init__(self, disco, dados):
        self.disco = disco
        self.dados = dados
    pass
