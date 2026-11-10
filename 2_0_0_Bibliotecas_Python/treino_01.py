import math

def recebe_numero():
    while True:
        try:
            numero = float(input("Digite o raio da mesa em metros: ").replace(",","."))
            break
        except:
            print("Valor inválido. Por favor, digite apenas números")
    return numero

def calcula_area(raio):
    area = math.pi * math.pow(raio, 2)
    return area

raio = recebe_numero()
area = round(calcula_area(raio), 2)

print("A área da mesa é: ", area, "mt²")