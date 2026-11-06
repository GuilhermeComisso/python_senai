#Inserir Senha

senha = 0

while senha !=1234:
    try:
        senha = int(input("Digite sua senha: "))
    except:
        print("Valor inválido. Por favor, digite apenas números. \n")

print("\nSenha digitada com sucesso!")