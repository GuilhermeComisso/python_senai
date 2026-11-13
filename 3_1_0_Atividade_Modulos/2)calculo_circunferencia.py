#Calcular Tubulação Obra

from mod_inputs import inp_float
import mod_sair
import math

def calcula(raio):
    circunferencia = 2 * math.pi * raio
    return circunferencia

start = True
while start:
    raio = inp_float("\nDigite a circunferência em cm: ")
    circunferencia=calcula(raio)
    print("A circunferência é: ", round(circunferencia,2), "cm.")
    start = mod_sair.finalizar()