try:
    idade = int(input("Digite sua idade em anos:"))
    if idade <=0:
        print("Idade Inválida")
    elif idade <=12:
        print("Você é uma criança")
    elif idade >=13 and idade <=17:
        print("Você é um adolescente")
    else:
        print("Você é um adulto")
    
except:
    print("Número Inválido. Por favor, digite apenas números!")