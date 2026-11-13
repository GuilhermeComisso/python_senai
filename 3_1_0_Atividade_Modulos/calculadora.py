import mod_inputs
import mod_operacoes
import mod_sair
# Utilizando as funções do módulo

def valida_opcao():
    while True:
        print("\nDigite + para adição")
        print("Digite - para subtração")
        print("Digite * para multiplicação")
        print("Digite / para divisão")
        operacao = mod_inputs.inp_str("\nDigite a operação desejada: ")
        if operacao in("+","-","*","/"):
            break
        else:
            print("Digite um operador válido. ")
    return operacao

def processa_calculo(num1, num2, operacao):
    match operacao:
        case "*":
            resultado = mod_operacoes.multiplicar(num1, num2)
        case "/":
            resultado = mod_operacoes.dividir(num1, num2)
        case "+":
            resultado = mod_operacoes.somar(num1, num2)
        case "-":
            resultado = mod_operacoes.subtrair(num1, num2)
    return resultado

start = True
while start:
    num1 = mod_inputs.inp_float("\nDigite seu primeiro número: ")
    num2 = mod_inputs.inp_float("Digite seu segundo número: ")
    operacao = valida_opcao()
    resultado = processa_calculo(num1, num2, operacao)

    print("O valor de", num1, operacao, num2, "é = ", resultado)

    start = mod_sair.finalizar()