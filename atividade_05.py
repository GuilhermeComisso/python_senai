#Recebendo Dados usando o input.

#Receber os dados num1
num01 = float(input("Digite o 1º número: ").replace(",","."))
num02 = int(input("Digite o 2º número: "))

#Processar as variáveis.
resultado = num01 ** num02

#Visualizar / Mostrar / Imprimir
print("O Valor de", num01, "elevado a pontência (^)", num02, "é =", resultado)