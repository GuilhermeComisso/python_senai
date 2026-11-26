import mod_inputs
import mod_msg

def recebe_opcao():
    while True:
        mod_msg.embalagem()
        opcao = mod_inputs.recebe_int("Digite uma opção: ")
        if opcao in(0, 1, 2):
            break
        else:
            print("Opção Inválida!\n")
    return opcao    

def escolhe_embalagem(opcao):
    embalagem = ["CAIXA PAPELÃO", "CAIXA CONTAINER"]
    return embalagem[opcao-1]

def main():
    start = True
    while start:
        opcao = recebe_opcao()
        if opcao != 0:
            embalagem = escolhe_embalagem(opcao)
            print("A embalagem é", aeroporto)

        else:    
            break
        
        #start = mod_finaliza.finaliza_programa()

if __name__ == "__main__":
    main()