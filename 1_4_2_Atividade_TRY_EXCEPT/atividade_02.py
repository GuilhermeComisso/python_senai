try:
    num1 = float(input("Digite seu nome completo:").replace(",", "."))
    num2 = float(input("Digite sua idade em anos:").replace(",", "."))
    resultado = num1 + num2

    print ("A soma de", num1, "+", num2, "é igual a:", resultado)

except:
    print("Valor inválido. Por favor, insira um número válido.")