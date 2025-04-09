from datetime import datetime
import pytz

# Armazenar depósitos, saques e saldo
depositos = []
saques = []
saldo = 0.0

# Limite de transações diárias
transacoes_diarias = 10
saque_realizado = 0 #podendo chegar somente em 3, havendo incremento a cada operação
data = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Função para depositar dinheiro
def depositar(valor):
    global saldo, transacoes_diarias

    if transacoes_diarias <= 0:
        print("Limite de transações diárias atingido. Volte amanhã!")
        return

    if valor > 0:
        depositos.append(valor)
        saldo += valor
        transacoes_diarias -= 1
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    else:
        print("Não foi possível depositar. O valor deve ser maior que zero.")

# Função para sacar dinheiro
def sacar(valor):
    global saldo, saque_realizado, transacoes_diarias

    if transacoes_diarias <= 0:
        print("Limite de transações diárias atingido. Volte amanhã!")
        return

    if saque_realizado < 3: 
        if valor <= 500:  
            if saldo >= valor:  
                saques.append(valor)
                saldo -= valor
                saque_realizado += 1
                transacoes_diarias -= 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Não foi possível sacar. Saldo insuficiente.')
        else:
            print('O valor do saque não pode ser maior que R$ 500,00.')
    else:
        print('Você já atingiu o limite máximo de saques por dia. Volte amanhã!')

# Função para exibir o extrato
def extrato():
    print('\n ------- EXTRATO -------')
    
    if not depositos and not saques:
        print('Não há movimentações!')
    
    else:
        for deposito in depositos:
            print(f'DEPÓSITO: R$ {deposito:.2f} - Data/Hora: {deposito[1].strftime("%d/%m/%Y %h:%m:%s")}')
        
        for saque in saques:        
            print(f'SAQUE: R$ {saque:.2f} - Data/Hora: {saque[1].strftime("%d/%m/%Y %h:%m:%s")}')

    print(f'Saldo atual: R$ {saldo:.2f}')

# Função para exibir o menu e interagir com o usuário
def menu():
    while True:
        print('\n--- MENU ---')
        print('1. DEPOSITAR')
        print('2. SACAR')
        print('3. EXTRATO')
        print('4. SAIR')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            valor = float(input('Digite o valor do depósito: '))
            depositar(valor)
        elif opcao == '2':
            valor = float(input('Digite o valor do saque: '))
            sacar(valor)
        elif opcao == '3':
            extrato()
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    menu()