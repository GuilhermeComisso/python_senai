from mod_inputs import inp_str

def finalizar():
    while True:
        try:
            opcao = inp_str("\nDeseja finalizar o programa? Digite S para [SIM] ou N para Executar novamente o programa. ")
            if opcao in("s", "S") or opcao in("n", "N"):
                break
            else:
                print("Opção inválida!\n")
        except:
            print("Valor inválido!")
    if opcao in("s", "S"):
        print("\nPrograma encerrado. ")
        return False
    else:
        return True