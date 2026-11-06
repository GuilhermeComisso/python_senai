#Criar - Calculadora

try:
    num1 = float(input("Digite o primeiro número: ").replace(",","."))
except:
    print ("Valor inválido para o primeiro número! ")

try:
    num2 = float(input("Digite o segundo número: ").replace(",","."))
except:
    print ("Valor inválido para o segundo número! ")

try:
    print("Dgite uma das operações a seguir: \n")
    print("Para multiplicação digite: *")
    print("Para divisão digite: /")
    print("Para adição digite: +")
    print("Para subtração digite: -")

    operador = str(input("Digite uma operação acima: "))
except:
    print("Operador Inválido")

match operador:
    case "*":
        resultado = num1 * num2
        print(num1, operador, num2,"é = ", resultado)
    case "/":
        resultado = num1 / num2
        print(num1, operador, num2,"é = ", resultado)
    case "+":
        resultado = num1 + num2
        print(num1, operador, num2,"é = ", resultado)
    case "-":
        resultado = num1 - num2
        print(num1, operador, num2,"é = ", resultado)
    case "_":
        print("Operador Inválido")