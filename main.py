class Departamento:
    def __init__(self,Departamento):
        self.Departamento = Departamento
    pass

class Funcionario:
    def __init__(self, ID, Nome, Matricula, Cargo, Departamento, Salario):
        self.ID = ID
        self.Nome = Nome
        self.Matricula = Matricula
        self.Cargo = Cargo
        self.Departamento = Departamento
        self.Salario = Salario
    pass

class Gerente:
    def __init__(self, ID, Nome, Matricula, Cargo, Departamento, Salario):
        self.ID = ID
        self.Nome = Nome
        self.Matricula = Matricula
        self.Cargo = Cargo
        self.Departamento = Departamento
        self.Salario = Salario
    pass

class Disco:
    def __init__(self, disco, dados):
        self.disco = disco
        self.dados = dados
    pass