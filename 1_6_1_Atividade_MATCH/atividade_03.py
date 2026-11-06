#Criar - Programa Bancário

try:
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    num = str(input("Digite uma opção acima: "))
    match num:
        case"1":
            print("Consultar Saldo")
            print("Saldo em conta: R$1000.00")
        case"2":
            print("Depositar")
        case"3":
            print("Sacar")
        case"4":
            print("Sair")

except:
    print("Número inválido, por favor digite um número válido")