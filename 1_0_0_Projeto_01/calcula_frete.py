import mod_inputs
import mod_msg

def receber_opcao():
    while True:
        mod_msg.msg_calcula_frete()
        opcao = mod_inputs.recebe_int("Digite a opcao desejada: ")
        if opcao in(0,1,2,3,4,5):
            break
        else:
            print("Opção invalida!!\n")
    return opcao

def escolhe_aeroporto(opcao):
    aeroporto = ["CONGONHAS/SP", "GUARULHOS/SP", "CAMPO DE MARTE/SP", "PINTO MARTINS/CE", "EDUARDO GOMES/AM"]
    return aeroporto[opcao-1]


def escolhe_distancia(opcao):
    distancia = [102, 112, 98, 2922, 6294,]
    return distancia[opcao-1]

def main():
    start = True
    while start:
        opcao = receber_opcao()
        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)
            print("O aeroporto é", aeroporto)
            print("A distância é", distancia, "km" )

        else:    
            break

def escolhe_embalagem():
    while True:
        print("\n--- Tipo de Embalagem ---")
        print("1 - Caixa de Papelão")
        print("2 - Caixa Container")
        tipo = mod_inputs.recebe_int("Escolha a embalagem: ")
        if tipo in (1, 2):
            return tipo
        print("Opção de embalagem inválida!!\n")

def calcular_frete(distancia):
    tipo = escolhe_embalagem()

    if tipo == 1:
        unidade = "metros (m)"
        fator = 0.26
    else:
        unidade = "centímetros (cm)"
        fator = 0.37

    # Observação: se o seu mod_inputs tiver uma função para decimal (ex: recebe_float),
    # use-a no lugar de float(input(...)) para manter o padrão do seu projeto.

    y = mod_inputs.recebe_float(f"Digite a Comprimento em {unidade}: ")
    x = mod_inputs.recebe_float(f"Digite a Largura em {unidade}: ")
    z = mod_inputs.recebe_float(f"Digite a Profundidade em {unidade}: ")
    w = mod_inputs.recebe_float("Digite o Peso em Kg: ")
   
    custo = ((y * x * z * w) * (1 + fator)) * (1 + (distancia * 9.8))
    return custo

def main():
    while True:
        opcao = receber_opcao()
        if opcao == 0:
            break

        aeroporto = escolhe_aeroporto(opcao)
        distancia = escolhe_distancia(opcao)
        valor_frete = calcular_frete(distancia)

        print(f"\nAeroporto de destino: {aeroporto}")
        print(f"Distância: {distancia} km")
        print(f"Custo total do frete: R$ {valor_frete:,.2f}\n")
        break

if __name__ == "__main__":
    main()