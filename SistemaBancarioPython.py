
import datetime

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

menu = """

    [d] Depositar \n
    [s] Sacar \n
    [e] Extrato \n
    [q] Sair

"""

# {PI:.2f}

while True:

    opcao = input(menu)

    if opcao == "d":

        v_deposito = int(input("Valor para deposito: \n"))

        if v_deposito < 1:
            print("Atenção, insira um valor valido!")
        else:
            saldo  += v_deposito
            print(f"Saldo atual \n R$:{saldo:.2f}")


    elif opcao == "s":

        if numero_saque == LIMITE_SAQUE:
            print("Limite de saque diário atingido!")

        else:

            v_saque = int(input("Valor que deseja sacar: \n"))

            if v_saque > limite:
                print("Atenção, limite de saque (R$ 500,00) excedido!")
            else:
                saldo -= v_saque
                numero_saque += 1
                extrato += f"saque: R$ {v_saque:.2f}"
                print(f"Saldo atual: R$:{saldo:.2f}")


    elif opcao == "e":

        print("\n ------------------------EXTRATO------------------------")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$: {saldo:.2f} \n \n Data: {datetime.datetime.now()}")
        print("-----------------------------------------------------------")
    
    
    elif opcao == "q":
        break
    else:
        print("Insira um valor valido!")
