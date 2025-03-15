# armazenar depósitos e saques
depositos = []
saques = []
saldo = 0.0

#Operação depósito

def depositar(valor):
    global saldo
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    else:
        print("não foi possivel depositar, tente novamente!")


#Operação de saque conferir se não ultrapassou de 3 no dia, impor o limite de R$ 500,00 e se há saldo sufiviente.

saque_realizado = 0

def sacar(valor):
    global saldo, saque_realizado
    if saque_realizado < 3:
        if valor <= 500:
            if saldo >= valor:
                saques.append(valor)
                saldo -= valor
                saque_realizado += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Não foi possivel sacar dinheiro por falta de saldo.')
        else:
            print('O valor do saque não pode ser maior que R$500,00.')
    else:
        print('Você já atingiu o maximo de saques por dia, volte amanhã!')

#Operação extrato

def extrato():
    print('\n ------- EXTRATO -------')
    if not depositos and not saques:
        print('Não há movimentações!')
    else:
        for deposito in depositos:
            print(f'DEPÓSITO: R$ {deposito:.2f}')
        for saque in saques:
            print(f'Saque: R$ {saque:.2f}')
    print(f'Salso atual: R$ {saldo:.2f}')



#Escolha do ususario da operação:

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