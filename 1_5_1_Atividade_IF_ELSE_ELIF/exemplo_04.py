#Temperaturas

try:
    valor= float(input("Digite a temperatura em °C:").replace(",","."))
    if valor <0:
        print(valor, "°C")
        print("Congelante")
    elif valor >=0 and valor <=15:
        print(valor, "°C")
        print("Frio")
    elif valor >15 and valor <=30:
        print(valor, "°C")
        print("Agradável")
    else:
        print(valor ,"°C")
        print("Muito Quente")

except:
    print("Digite apenas números")