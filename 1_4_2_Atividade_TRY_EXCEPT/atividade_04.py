try:
    nome = str(input("Digite o nome do aluno:"))
    num1 = float(input("Digite o valor da 1ª nota:").replace(",", "."))
    num2 = float(input("Digite o valor da 2ª nota:").replace(",", "."))
    num3 = float(input("Digite o valor da 3ª nota:").replace(",", "."))
    resultado = (num1 + num2 + num3) / 3

    print("A média do aluno", nome, "é:", resultado, "pontos")
    
    if resultado >= 7:
        print("O aluno", nome, "foi aprovado!")
    else:
        print("O aluno", nome, "foi reprovado!")    

except:
    print("Valor inválido. Por favor, insira um número válido.")