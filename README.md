### Realização do primeiro desafio de código da DIO

Meu primeiro desafio de código fazendo um simples sistema bancário que realiza três transações, Depósito, Saque e Extrato. Sendo elas:

OPERAÇÃO DE DEPOSITO

- ter o usuario
- deposito deve ser armazenado em uma variavel, input de deposito
- extrato deve exibir o que vem de depósito
- não posso depositar menos de 100 reais

OPERAÇÃO DE SAQUE

- só posso permitir 3 saques diarios 
- limite de 500 reais por saque 
- se o usuario nao tiver o saldo em conta exibir mensagem na tela 
- saque deve ser armazenado em uma variavel
- extrato deve exibir os saques

OPERAÇÃO DE EXTRATO

- listar todos os depositos e saques
- ter o saldo atual da conta 
- os valores devem ser exibidos no formato R$xxx,xx


## Novas Funcionalidades do Sistema Bancário
Este sistema bancário implementa várias funcionalidades para gerenciar contas e usuários. As funcionalidades são divididas em operações básicas de transação, além de funções para a criação e gestão de usuários e contas. Abaixo estão as descrições das principais funcionalidades:

DEPOSITO
Função: depositar

Descrição: Realiza um depósito na conta do usuário.
Parâmetros:
saldo (float): O saldo atual da conta.
valor (float): O valor a ser depositado.
extrato (str): O extrato das transações da conta.
Retorno:
saldo (float): O saldo atualizado após o depósito.
extrato (str): O extrato atualizado com a transação de depósito.

SAQUE
Função: sacar

Descrição: Realiza um saque da conta do usuário.
Parâmetros:
saldo (float): O saldo atual da conta.
valor (float): O valor a ser sacado.
extrato (str): O extrato das transações da conta.
limite (float): O limite máximo permitido para um saque.
numero_saques (int): O número atual de saques realizados no dia.
limite_saques (int): O número máximo permitido de saques por dia.
Retorno:
saldo (float): O saldo atualizado após o saque.
extrato (str): O extrato atualizado com a transação de saque.
numero_saques (int): O número atualizado de saques realizados no dia.

EXTRATO
Função: exibir_extrato

Descrição: Exibe o extrato da conta do usuário.
Parâmetros:
saldo (float): O saldo atual da conta.
extrato (str): O extrato das transações da conta.
Retorno: Não há retorno. Apenas exibe o extrato e o saldo atual.

USUARIO
Função: criar_usuario

Descrição: Cria um novo usuário (cliente do banco) e o adiciona à lista de usuários.
Parâmetros:
usuarios (list): A lista atual de usuários.
Retorno:
usuarios (list): A lista atualizada de usuários após a adição do novo usuário.

CONTA CORRENTE
Função: criar_conta_corrente

Descrição: Cria uma nova conta corrente e a vincula a um usuário existente.
Parâmetros:
agencia (str): O número da agência (fixo: "0001").
contas (list): A lista atual de contas.
usuarios (list): A lista atual de usuários.
Retorno:
contas (list): A lista atualizada de contas após a criação da nova conta.

MAIN

Descrição: Gerencia o loop principal do programa, exibindo o menu e chamando as funções apropriadas com base na opção selecionada pelo usuário.
Operações Disponíveis:
Depositar
Sacar
Exibir Extrato
Criar Usuário
Criar Conta Corrente
Sair
Exemplo de Uso
O usuário escolhe uma opção do menu para realizar uma operação.
O sistema solicita os dados necessários para a operação escolhida.
O sistema atualiza os dados e exibe informações relevantes (como saldo e extrato).
O usuário pode continuar realizando operações até escolher a opção de sair.
Nota
O número da conta corrente é gerado sequencialmente, começando em 1, e o número da agência é fixo ("0001"). Um usuário pode ter várias contas, mas cada conta pertence a apenas um usuário.

