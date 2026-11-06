def soma(nm1, nm2):
    soma = nm1 + nm2
    return soma

start = True
while start:
    try:
        num1 = float(input("Digite o primeiro número: ").replace(",","."))
        start = False
    except:
        print("Valor inválido! Por favor, digite apenas números. ")

start = True
while start:
    try:
        num2 = float(input("Digite o segundo número: ").replace(",","."))
        start = False
    except:
        print("Valor inválido! Por favor, digite apenas números. ")

resultado = soma(num1, num2)
print(f"O resultado da soma é: {resultado}")