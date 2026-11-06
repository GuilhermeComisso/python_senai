#Criar - Dias da Semana

try:
    nota = int(input("Digite um número de 1 a 7: "))
    match nota:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3:
            print("Terça-Feia")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case 6:
            print("Sexta-Feira")
        case 7:
            print("Sábado")
        case _:
            print("Valor Inválido")

except:
    print("Número inválido, por favor digite um número válido")