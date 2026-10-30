try:
    num1 = float(input("Digite o valor do produto:").replace(",", "."))
    num2 = float(input("Digite percentual de desconto:").replace(",", "."))
    resultado = num1 - (num1 * num2 / 100)

    print ("O valor do produto com desconto é:", resultado)

except:
    print("Valor inválido. Por favor, insira um número válido.")