import getpass

def recebe_str(mensagem):
    while True:
        try:
           texto = str(input(mensagem))
           break
        except:
            print("Valor Invalido!")
    return texto 


def recebe_senha(mensagem):
    while True:
        try:
            senha = getpass.getpass(mensagem)
            break
        except:
            print("Valor Invalido!")
    return senha
                  