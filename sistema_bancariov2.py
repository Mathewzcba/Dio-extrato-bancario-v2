import time

# Lista de usuários
usuarios = []

class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.conta_corrente = ContaCorrente()

class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: {valor}")
            time.sleep(2)
            print(f'Depósito realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor <= self.limite and valor > 0:
            if self.numero_saques < self.LIMITE_SAQUES and self.saldo >= valor:
                self.saldo -= valor
                self.numero_saques += 1
                self.LIMITE_SAQUES -= 1
                self.extrato.append(f"Saque: {valor}")
                time.sleep(2)
                print('Saque realizado com sucesso.')
            elif self.numero_saques >= self.LIMITE_SAQUES:
                print('Você já utilizou o limite de saques diários.')
            elif self.saldo < valor:
                print('Você não tem saldo suficiente.')
        else:
            print('Valor de saque inválido.')

    def mostrar_extrato(self):
        print('GERANDO EXTRATO...')
        time.sleep(2)
        print(f"Seu saldo unificado é R${self.saldo}, limite total é R${self.limite} e você tem disponível {self.LIMITE_SAQUES} saques diários.")
        print(f'Suas últimas movimentações: {self.extrato}')

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_nascimento = input("Digite sua Data de nascimento:")
    usuario = Usuario(nome, cpf, data_nascimento)
    usuarios.append(usuario)
    print(f'Usuário {nome} criado com sucesso.')

def escolher_usuario():
    print('Selecione um usuário:')
    for i, usuario in enumerate(usuarios):
        print(f'{i} - {usuario.nome}')
    escolha = int(input('Digite o número do usuário: '))
    return usuarios[escolha]

while True:
    print('''SEJA BEM-VINDO AO BANCO DIO
    [0] - CRIAR USUÁRIO
    [1] - DEPÓSITO
    [2] - SAQUE
    [3] - EXTRATO
    [4] - SAIR''')
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 0:
        criar_usuario()

    elif opcao == 1:
        usuario = escolher_usuario()
        valor = int(input("DIGITE O VALOR QUE DESEJA DEPOSITAR, R$: "))
        usuario.conta_corrente.depositar(valor)

    elif opcao == 2:
        usuario = escolher_usuario()
        valor = int(input("DIGITE O VALOR QUE DESEJA SACAR, R$: "))
        usuario.conta_corrente.sacar(valor)

    elif opcao == 3:
        usuario = escolher_usuario()
        usuario.conta_corrente.mostrar_extrato()

    elif opcao == 4:
        print('Obrigado por utilizar o Sistema.')
        break

    else:
        print('Opção inválida, tente novamente.')
