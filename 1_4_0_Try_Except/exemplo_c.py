try:
    num1 = float(input("Digite um número:").replace(",", "."))
    num2 = float(input("Digite outro número:").replace(",", "."))
    resultado = num1 / num2
    print("O valor da divisão de", num1, "+", num2, "é=", resultado)

except ValueError:   
    print("Valor Inválido! Não foi possível realizar a divisão.")
except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero. Por favor, digite um número diferente de zero para o segundo valor.")