import pyfiglet

def msg_inicial():
    print ("Seja Bem Vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format ("Cota Frete", font="pagga")
    print(mensagem)


def msg_login_ini():
    print("#############################################################")
    print("<<<<<<<<<<<<<<<<<<<<< LOGAR NO SISTEMA >>>>>>>>>>>>>>>>>>>>>>")
    print("#############################################################\n")