def menu():
    return """ 
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[0] Sair
=> """

def depositar(*, saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
        print(f"Você depositou R${valor:.2f}!")
    elif valor < 100:
        print("O valor mínimo de depósito é R$100,00")
    else:
        print("A operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Você excedeu o limite de saques diários da conta, volte amanhã!")
    elif saldo < valor:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print("Você só pode sacar até R$500,00 por saque, tente novamente.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque de R${valor:.2f}\n"
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(*, saldo, extrato):
    print("Extrato")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
    print(f"Saldo atual: R${saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF!")
        return usuarios
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    return usuarios

def criar_conta_corrente(agencia, contas, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado!")
        return contas
    numero_conta = len(contas) + 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print(f"Conta corrente criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")
    return contas

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu())
        
        if opcao == "1":
            valor = float(input("Qual o valor que deseja depositar? "))
            saldo, extrato = depositar(saldo=saldo, valor=valor, extrato=extrato)
        
        elif opcao == "2":
            valor = float(input("Qual o valor que deseja sacar? "))
            saldo, extrato, numero_de_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_de_saques, limite_saques=LIMITE_SAQUES)
        
        elif opcao == "3":
            exibir_extrato(saldo=saldo, extrato=extrato)
        
        elif opcao == "4":
            usuarios = criar_usuario(usuarios)
        
        elif opcao == "5":
            contas = criar_conta_corrente(AGENCIA, contas, usuarios)
        
        elif opcao == "0":
            break
        
        else:
            print("Operação inválida, por favor selecione a operação desejada.")

if __name__ == "__main__":
    main()
