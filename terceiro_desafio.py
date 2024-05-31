class Transacao:
    def __init__(self, valor):
        self.valor = valor

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero):
        self.cliente = cliente
        self.numero = numero
        self.saldo = 0.0
        self.historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            print(f"Você depositou R${valor:.2f}!")
        else:
            print("A operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("Extrato")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações")
        else:
            for transacao in self.historico.transacoes:
                print(f"{transacao.__class__.__name__} de R${transacao.valor:.2f}")
        print(f"Saldo atual: R${self.saldo:.2f}")

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

def main():
    clientes = []
    contas = []
    while True:
        print("Menu:")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Criar Usuário")
        print("[5] Criar Conta Corrente")
        print("[6] Listar Contas")
        print("[0] Sair")
        opcao = input("=> ")
        
        if opcao == "1":
            cpf = input("Digite o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente is None:
                print("Cliente não encontrado!")
                continue
            conta = cliente.contas[0]  # assumindo que o cliente tem pelo menos uma conta
            valor = float(input("Qual o valor que deseja depositar? "))
            conta.depositar(valor)
        
        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente is None:
                print("Cliente não encontrado!")
                continue
            conta = cliente.contas[0]  # assumindo que o cliente tem pelo menos uma conta
            valor = float(input("Qual o valor que deseja sacar? "))
            conta.sacar(valor)
        
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente is None:
                print("Cliente não encontrado!")
                continue
            conta = cliente.contas[0]  # assumindo que o cliente tem pelo menos uma conta
            conta.exibir_extrato()
        
        elif opcao == "4":
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF (somente números): ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cliente = Cliente(nome, cpf, data_nascimento, endereco)
            clientes.append(cliente)
            print("Usuário criado com sucesso!")
        
        elif opcao == "5":
            cpf = input("Digite o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente is None:
                print("Cliente não encontrado!")
                continue
            numero_conta = len(contas) + 1
            conta = Conta(cliente, numero_conta)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print(f"Conta corrente criada com sucesso! Número da Conta: {numero_conta}")
        
        elif opcao == "6":
            for conta in contas:
                print(f"Número da Conta: {conta.numero}, Titular: {conta.cliente.nome}, CPF: {conta.cliente.cpf}")
        
        elif opcao == "0":
            break
        
        else:
            print("Operação inválida, por favor selecione a operação desejada.")

if __name__ == "__main__":
    main()
