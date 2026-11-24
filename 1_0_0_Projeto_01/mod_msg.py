import pyfiglet

def msg_inicial():
    print("Seja bem vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format("COTA-FRETE", font="pagga")
    print(mensagem)

def msg_login_ini():
    print("##############################")
    print("<<<<<< LOGAR NO SISTEMA >>>>>>")
    print("##############################\n")

def msg_menu_principal():
    print("##########################################################")
    print("<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("##########################################################\n")
    print("##### SAIR - 0 | CALCULADORA - 1 | CALCULA FRETE - 2 #####\n")

def msg_calc_ini():
    print("##############################")
    print("<<<<<<<< CALCULADORA >>>>>>>>>")
    print("##############################\n")

def msg_calcula_frete():
    print(" ESCOLHA UM DESTINO ")
    print(" SAIR - 0 >>")
    print(" CONGONHAS/SP - 1 ")
    print(" GUARULHOS/SP - 2 ")
    print(" CAMPO DE MARTE/SP - 3 ")
    print(" PINTO MARTINS/CE - 4 ") 
    print(" EDUARDO GOMES/AM - 5 \n")  

def msg_final_programa():
    print("#####################################################")
    print("<<<< OBRIGADO POR UTILIZAR O PROGRAMA COTA-FRETE >>>>")
    print("################# VOLTE SEMPRE !!!! #################\n")
