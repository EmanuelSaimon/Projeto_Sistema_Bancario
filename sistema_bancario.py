menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Qual valor deseja ser depositado: "))

        if valor > 0:
            saldo += valor
            print(f"\nR${valor:.2f} foi depositado!")
            extrato += f"\nR${valor:.2f} foi depositado!"
                    
        else:
            print("Operação falhou. Valor inválido")
            

    elif opcao == "S":
        valor = float(input("Qual valor deseja ser sacado: "))

        if valor > limite:
            print("Operação falhou. Valor excedeu o limite de saque")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou. Número máximo de saques diarios excedido")

        elif valor > saldo:
            print("Operação falhou. Saldo insuficiente")

        elif valor > 0:
            saldo -= valor
            print(f"\nR${valor:.2f} foi sacado!")
            extrato += f"\nR${valor:.2f} foi sacado!"
            numero_saques += 1

        else:
            print("Operação falhou. Valor inválido")

    elif opcao == "E":
        print("\n=====EXTRATO=====\n")
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"Saldo bancario: R${saldo:.2f}")

    elif opcao == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")