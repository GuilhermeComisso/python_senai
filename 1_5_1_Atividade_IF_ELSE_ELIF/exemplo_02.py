try:
    nota=float(input("Digite a nota do aluno:").replace(",","."))
    if nota <0 or nota >10:
        print("Nota inválida")
    elif nota >=0 and nota <5:
        print("Aluno reprovado")
    elif nota >=5 and nota <7:
        print("Aluno em recuperação")
    else:
        print("Aprovado")

except:
    print("Digite apenas números")