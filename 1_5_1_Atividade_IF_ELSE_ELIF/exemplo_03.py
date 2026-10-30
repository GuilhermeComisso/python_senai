#Loja - descontos

try:
    valor= float(input("Digite o valor da compra:").replace(",","."))
    if valor <0:
        print("Valor inválida")
    elif valor <=100:
        print("Sem desconto")
        print("O valor da compra é ", valor)
    elif valor >100 and valor <=500:
        vlr_desconto = valor*(1-(10/100))
        print("Desconto de 10%")
        print("O valor da compra com desconto de 10% é", vlr_desconto)
    elif valor >500:
        vlr_desconto = valor*(1-(15/100))
        print("Desconto de 15%")
        print("O valor da compra com desconto de 15% é", vlr_desconto)

except:
    print("Digite apenas números")