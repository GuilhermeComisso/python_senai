#Temperaturas

try:
    valor= float(input("Digite a temperatura em °C:").replace(",","."))
    if valor <0:
        print("A temperatura esta em", valor, "°C")
        print("Congelante")
    elif valor >=0 and valor <=15:
        print("A temperatura esta em", valor, "°C")
        print("Frio")
    elif valor >15 and valor <=30:
        print("A temperatura esta em", valor, "°C")
        print("Agradável")
    else:
        print("A temperatura esta em", valor ,"°C")
        print("Muito Quente")

except:
    print("Digite apenas números")