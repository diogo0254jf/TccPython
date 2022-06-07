class Modo_de_Acesso():
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

    def contratar(self):
        if self.modoAcesso == 'Acesso ao disco':
            if self.ID and self.Nome and self.Matricula and self.Cargo and self.Departamento and self.Salario:
                with open("Funcionario.txt",'a', encoding='utf-8') as arquivo:
                    arquivo.write(f'Funcionario \nNome: {self.Nome}\nMatricula: {self.Matricula}\nCargo: {self.Cargo}\nDepartamento: {self.Departamento}\nSalário: {self.Salario}\n\n')
                    print(f'Funcionário {self.Nome} contratado com sucesso!')
                print(f'Funcionário {self.Nome} contratado com sucesso!')
            else:
                print('Erro ao contratar funcionário!\nMotivo: Está faltando dados para a contratação')
        else:
            print('Erro ao contratar funcionário!\nMotivo: O modo de acesso não é válido')

    def recuperar(self):
        if self.modoAcesso == 'Acesso ao disco':
            with open("Funcionario.txt",'a', encoding='utf-8') as arquivo:
                print(arquivo.read())
        else:
            print('Erro ao recuperar funcionário!\nMotivo: O modo de acesso não é válido')

class Departamento(Funcionario):
    def __init__(self, Departamento, ID, Nome, Gerente):
        self.Departamento = Departamento
        self.ID = ID
        self.Nome = Nome
        self.Gerente = Gerente
    
    def NovoDepartamento(self):
        with open("Departamento.txt",'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Departamento: {self.Departamento} \nNome: {self.Nome}\nGerente: {self.Gerente}\n\n')
            print(f'Departamento {self.Nome} criado com sucesso!')

class Gerente(Funcionario):
    def __init__(self, ID, Nome, Matricula, Cargo, Departamento, Salario: float, modoAcesso: str):
        self.Salario = (Salario * 0.84) + (Salario * 0.5)

    def novo_gerente(self):
        with open("Gerente.txt",'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Funcionario \nNome: {self.Nome}\nMatricula: {self.Matricula}\nCargo: {self.Cargo}\nDepartamento: {self.Departamento}\nSalário: {self.Salario}\n\n')
            print(f'Gerente criado com sucesso!')

class Caixa():
    def __init__(self, ID, Nome, Departamento, Salario):
        self.ID = ID
        self.Nome = Nome
        self.Departamento = Departamento
        self.Salario = Salario

    def novo_caixa(self):
        with open("Caixa.txt",'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Funcionario \nNome: {self.Nome}\nDepartamento: {self.Departamento}\nSalário: {self.Salario}\n\n')
            print(f'Caixa criado com sucesso!')

    def registrar_venda(self):
        with open("Caixa.txt",'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Venda \nID: {self.ID}\nProduto: {self.produto}\nQuantidade: {self.quantidade}\nValor: {self.valor}\n\n')
            print(f'Venda registrada com sucesso!')
    def Deletar_venda():
        with open("Caixa.txt",'r', encoding='utf-8') as arquivo:
            arquivo.write(f'Venda deletada!\n\n')
            print(f'Venda deletada!')
    def iniciar_caixa():
        with open("Caixa.txt",'r', encoding='utf-8') as arquivo:
            arquivo.write(f'Caixa aberto!\n\n')
            print(f'Caixa aberto!')

    def fechar_caixa():
        with open("Caixa.txt",'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Caixa fechado!\n\n')
            print(f'Caixa fechado!')


def contratar_Funcionario():
    ID = input('Digite o ID do funcionário: ')
    Nome = input('Digite o nome do funcionário: ')
    Matricula = input('Digite a matricula do funcionário: ')
    Cargo = input('Digite o cargo do funcionário: ')
    Departamento = input('Digite o departamento do funcionário: ')
    Salario = float(input('Digite o salário do funcionário: '))
    acesso = input('Digite o modo de acesso do funcionário\n1 - Acesso ao disco\n2 - Acesso ao dados')
    if acesso == '1':
        modoAcesso = 'Acesso ao disco'
    elif acesso == '2':
        modoAcesso = 'Acesso ao dados'
    else:
        print('Modo de acesso inválido!')
    
    contratar = Funcionario(ID, Nome, Matricula, Cargo, Departamento, Salario, modoAcesso)
    contratar.contratar()
    print(ID, Nome, Matricula, Cargo, Departamento, Salario, modoAcesso)
    
def definir_ao_Departamento():
    ID = input('Digite o ID do funcionário: ')
    Gerente = input('Digite o nome do Gerente: ')
    Departamento = input('Digite o departamento do funcionário: ')
    definir = Departamento(Departamento, ID, Gerente)
    definir.NovoDepartamento()

def Promover_a_Gerente():
    ID = input('Digite o ID do funcionário: ')
    novogerente = Gerente(ID)
    novogerente.novo_gerente()

def Listar_funcionarios():
    with open("Funcionario.txt",'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

def Atualizar_dados_funcionario():
    ID = input('Digite o ID do funcionário: ')
    Nome = input('Digite o nome do funcionário: ')
    Matricula = input('Digite a matricula do funcionário: ')
    Cargo = input('Digite o cargo do funcionário: ')
    Departamento = input('Digite o departamento do funcionário: ')
    Salario = float(input('Digite o salário do funcionário: '))
    acesso = input('Digite o modo de acesso do funcionário\n1 - Acesso ao disco\n2 - Acesso ao dados\n')
    if acesso == '1':
        modoAcesso = 'Acesso ao disco'
    elif acesso == '2':
        modoAcesso = 'Acesso ao dados'
    else:
        print('Modo de acesso inválido!')
    
    atualizar = Funcionario(ID, Nome, Matricula, Cargo, Departamento, Salario, modoAcesso)
    atualizar.contratar()
    print(ID, Nome, Matricula, Cargo, Departamento, Salario, modoAcesso)

def Registrar_Venda():
    valor = float(input('Digite o valor do produto: '))
    venda = Caixa(valor)
    venda.novo_caixa()

def Atualizar_venda():
    ID = input('Digite o ID da venda: ')
    produto = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))
    valor = float(input('Digite o valor do produto: '))

    venda = Caixa(ID, produto, quantidade, valor)
    venda.registrar_venda()

def Deletar_venda():
    ID = input('Digite o ID da venda: ')
    venda = Caixa(ID)
    venda.deletar_venda()

def Recuperar_por_ID():
    ID = input('Digite o ID do funcionário: ')
    recuperar = Funcionario(ID)
    recuperar.recuperar()

def Listar_venda():
    with open("Caixa.txt",'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

def Calcular_montante_de_Venda():
    with open("Caixa.txt",'a', encoding='utf-8') as arquivo:
        montante = 0
        for linha in arquivo:
            montante += float(linha)

def Iniciar_Caixa():
    caixa = Caixa()
    caixa.iniciar_caixa()

def Fechar_Caixa():
    caixa = Caixa()
    caixa.fechar_caixa()

entrada = input("Minhas funçoes!\nACESSO AO DISCO\n1 - Contratar Funcionario\n2 - Definir ao Departamento\n3 - Promover a Gerente\n4 - Listar funcionarios\n5 - Atualizar dados funcionarion\nACESSO AOS DADOS\n6 - Salvar venda\n7 - Atualizar venda\n8 - Deletar venda\n9 - Recuperar por ID\n10 - Listar venda\n11 - Registrar Venda\n12 - Calcular montante de Venda\n13 - Iniciar Caixa\n14 - Fechar Caixa\n0 - Sair\n")

if entrada == '1':
    contratar_Funcionario()
elif entrada == '2':
    definir_ao_Departamento()
elif entrada == '3':
    Promover_a_Gerente()
elif entrada == '4':
    Listar_funcionarios()
elif entrada == '5':
    Atualizar_dados_funcionario()
elif entrada == '6':
    Atualizar_venda()
elif entrada == '7':
    Deletar_venda()
elif entrada == '8':
    Recuperar_por_ID()
elif entrada == '9':
    Listar_venda()
elif entrada == '10':
    Registrar_Venda()
elif entrada == '11':
    Calcular_montante_de_Venda()
elif entrada == '12':
    Iniciar_Caixa()
elif entrada == '13':
    Fechar_Caixa()
elif entrada == '0':
    print('Saindo...')