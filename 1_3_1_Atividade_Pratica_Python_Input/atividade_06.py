#Recebendo Dados usando o input.

#Receber os dados num1
num01 = int(input("Digite o 1º número: ").replace(",","."))
num02 = int(input("Digite o 2º número: ").replace(",","."))

#Processar as variáveis.
resultado = ((num01 + num02) **(1/2))     

#Visualizar / Mostrar / Imprimir
print("O Valor da Raiz Quadrada de ", num01, +, num02 "é =", resultado)