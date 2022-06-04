class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contrata(self, funcionario):
        self.funcionarios.append(funcionario)

    def lista_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)
            
class Modo_de_Acesso:
    def __init__(self, modoAcesso):
        self.modoAcesso = modoAcesso
        
class Funcionario(Modo_de_Acesso):
    def __init__(self, ID, Nome, Matricula, Cargo, Departamento, Salario: float, modoAcesso: str):
        self.ID = ID
        self.Nome = Nome
        self.Matricula = Matricula
        self.Cargo = Cargo
        self.Departamento = Departamento
        self.Salario = Salario
        self.modoAcesso = modoAcesso

    def contratar(self,modoAcesso):
        if self.modoAcesso == 'Acesso ao disco':
            if self.ID and self.Nome and self.Matricula and self.Cargo and self.Departamento and self.Salario:
                with open('funcionario.txt','w') as testzada:
                    testzada.write('Ficha de contratação funcionar') # insira seu conteúdo
                    #arquivo.append(f'Nome: {self.Nome}')   # insira seu conteúdo
                    #arquivo.append(f'Matricula: {self.Matricula}')   # insira seu conteúdo
                    #arquivo.append(f'Cargo: {self.Cargo}')   # insira seu conteúdo
                    #arquivo.append(f'Departamento: {self.Departamento}')   # insira seu conteúdo
                    #arquivo.append(f'Salário: {self.Salario}')   # insira seu conteúdo
                    #arquivo.close()
                print(f'Funcionário {self.Nome} contratado com sucesso!')
            else:
                print('Erro ao contratar funcionário!\nMotivo: Está faltando dados para a contratação')
        else:
            print('Erro ao contratar funcionário!\nMotivo: O modo de acesso não é válido')

class Departamento(Funcionario):
    def __init__(self, Departamento, ID, Nome, Gerente):
        self.Departamento = Departamento
        self.ID = ID
        self.Nome = Nome
        self.Gerente = Gerente
    
class Gerente(Funcionario):
    def __init__(self, Salario: float,Departamento):
        self.Departamento = Departamento
        self.Salario = (Salario * 0.84) + (Salario * 0.5)


teste = Funcionario('1','João','12345','Programador','TI','R$ 1.000,00','Acesso ao disco')
teste.contratar('Acesso ao disco')