#Calcular desconto de um produto

def calcular_desconto(valor, desconto):
    valor_desconto = valor - (valor * desconto / 100)
    return valor_desconto

def receber_numero(mensagem):
    start = True
    while start:
        try:
            numero = float(input(mensagem).replace(",","."))
            start = False
        except:
            print("Valor inválido! Por favor, digite apenas números. ")
    return numero

valor = receber_numero("Digite o valor do produto: ")
desconto = receber_numero("Digite o desconto em porcentagem: ")

resultado = calcular_desconto(valor, desconto)
print("O valor do produto é = ", valor)
print("O porcentagem do desconto é = ", desconto, "%")
print("O valor da compra com desconto é = ", resultado)