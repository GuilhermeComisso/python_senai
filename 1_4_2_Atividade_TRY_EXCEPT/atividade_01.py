try:
    Nome = str(input("Digite seu nome completo:"))
    Idade = int(input("Digite sua idade em anos:"))

    print ("O nome do aluno é:", Nome)
    print ("Sua idade é:", Idade," anos")
except:
    print("Erro: Por favor, insira um valor válido para a idade.")