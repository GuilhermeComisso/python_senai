try:
    num1 = int(input("Digite um número Inteiro:"))
    num2 = int(input("Digite outro número Inteiro:"))
    resultado = num1 + num2
    print("O valor da some de", num1, "+", num2, "é", resultado)

except:    
    print("Valor Inválido! Digite apenas um número inteiro.")