def soma(nm1, nm2):
    soma = nm1 + nm2
    return soma

def receber_numero(mensagem):
    start = True
    while start:
        try:
            numero = float(input(mensagem).replace(",","."))
            start = False
        except:
            print("Valor inválido! Por favor, digite apenas números. ")
    return numero

num1 = receber_numero("Digite o primeiro número: ")
num2 = receber_numero("Digite o segundo número: ")

resultado = soma(num1, num2)
print("O valor da soma é = ", resultado)