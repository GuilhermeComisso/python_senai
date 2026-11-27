import mod_msg
import mod_inputs
import calculadora
import calcula_frete

def recebe_opcao():
    while True:
        mod_msg.msg_menu_principal()
        opcao = mod_inputs.recebe_int("Digite uma opção do menu: ")
        match opcao:
            case 0:
                break
            case 1:
                calculadora.main() 
            case 2:
                calcula_frete.main()
            case _:
                print("Opção inválida!\n")

def main():
    while True:
        #mod_msg.msg_menu_principal()
        recebe_opcao()
        mod_msg.msg_final_programa()
        break