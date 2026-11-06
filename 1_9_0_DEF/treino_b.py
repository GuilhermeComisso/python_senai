#Calcular a média do aluno

def calcular_nota(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def receber_numero(mensagem):
    start = True
    while start:
        try:
            numero = float(input(mensagem).replace(",","."))
            start = False
        except:
            print("Valor inválido! Por favor, digite apenas números. ")
    return numero

nota1 = receber_numero("Digite a primeira nota (de 0 a 10): ")
nota2 = receber_numero("Digite a segunda nota (de 0 a 10): ")
nota3 = receber_numero("Digite a terceira nota (de 0 a 10): ")

resultado = calcular_nota(nota1, nota2, nota3)
print("O valor da média é = ", resultado)

if resultado >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")