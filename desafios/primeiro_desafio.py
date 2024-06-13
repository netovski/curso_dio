menu = """ 

[1] Depositar
[2] Sacar
[3] Extrato 
[0] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao  == "1":
        print("Depósito")
        deposito = float(input("Qual o valor que deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            print(f"Você depositou R${deposito:.2f}!")
            extrato += f"Depósito de R${deposito:.2f}\n"
            
        elif deposito < 100:
            print("O valor mínimo de depósito é R$100,00")
            
        else:
            print("A operação falhou! O valor informado é inválido.")

        
    elif opcao == "2":
        print("Saque")
        while numero_de_saques >= LIMITE_SAQUES:
            print("Você excedeu o limite de saques diários da conta, volte amanhã!")
            break
        saque = float(input("Qual o valor que deseja sacar? "))     
        if saldo < saque:
            print("Saldo insuficiente para realizar o saque.")
        elif saque > 500:
            print("Você só pode sacar até R$500,00 por saque, tente novamente.")
        else:
            print(f"Saque de R${saque:.2f} realizado com sucesso!")
            saldo -= saque
            numero_de_saques += 1
            extrato += f"Saque de R${saque:.2f}\n"


    elif opcao == "3":
        print("Extrato")
        
        if not extrato:
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
                
        
    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione a operação desejada.")