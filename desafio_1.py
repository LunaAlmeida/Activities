menu ="""
    Escolha uma opção:

    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [4] - Sair
"""

saldo = 0
saque = []
deposito = []
limite_saque = 3

while(True):
    print(menu)
    opcao = int(input())


    if(opcao == 1):
        valor_deposito = float(input("Digite o valor do depósito: "))
        while(valor_deposito <= 0):
            print("Apenas valores positivos podem ser depositados. Digite outro valor.")
            valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        deposito.append(valor_deposito)

    elif(opcao == 2):
        if(limite_saque == 0):
            print("Limite de saque diário atingido! Volte em 24 horas.")
            continue
        elif(saldo <= 0):
            print("Saldo insuficiente!")
            continue
        else:
            limite_saque -= 1
            sacar = float(input("Digite o valor que deseja sacar: "))
            if(sacar > saldo):
                print("Saldo insuficiente!")
                continue
            while(sacar < 0):
                print("Não é possível sacar valores negativos. Digite um novo valor!")
                sacar = float(input("Digite o valor que deseja sacar: "))
            while(sacar > 500):
                print("O limite máximo de saque é R$ 500,00. Digite outro valor.")
                sacar = float(input("Digite o valor que deseja sacar: "))
            saque.append(sacar)
            saldo -= sacar

    elif(opcao == 3):
        print(20*'-', end='')
        print(" EXTRATO ", end='')
        print(20*'-')
        if((not deposito) & (not saque)):
            print("Não foram realizadas movimentações na conta.")
        else:
            for i, valor in enumerate(deposito):
                print(f"Deposito {i+1}: R$ {valor:.2f}")

            print(49*'-')
            for i, valor in enumerate(saque):
                print(f"Saque {i+1}: R$ {valor:.2f}")

        print(49*'-')
        print(f"Saldo total: R$ {saldo:.2f}")
        print(49*'-')

    elif(opcao == 4):
        print("Agradecemos. Volte sempre!")
        break

    else:
        print("Operação inválida.")

