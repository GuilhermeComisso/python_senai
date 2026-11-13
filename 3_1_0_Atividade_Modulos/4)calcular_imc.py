import mod_inputs
import mod_operacoes
import mod_sair
import math

# Utilizando as funções do módulo

def calcula(altura, peso):
    imc = peso / math.pow(altura, 2)
    return imc

def classificacao(imc, idade):
    while True :
        if idade < 20:
            print ("Idade invalida, digite uma idade acima de 20 anos ")
        else:
            if idade >=20 and idade <=60: 
                if imc <18.5:
                    mensagem = "baixo peso"
                elif imc >=18.5 and imc <25:
                    mensagem = "peso normal"
                elif imc >=25 and imc <30: 
                    mensagem ="sobrepeso"   
                else:
                    mensagem ="obesidade"
            else:
                if imc <22:
                    mensagem = "baixo peso"
                elif imc >=22 and imc <=27:
                    mensagem = "peso normal"
                elif imc >27 and imc <30: 
                    mensagem ="sobrepeso"   
                else:
                    mensagem = "obesidade"
            break    
    return mensagem

def valida_idade ():
    while True :
       idade = mod_inputs.inp_int("Digite sua idade em anos: ")
       if idade >=20:
           break
       else:
           print ("Idade invalida, digite uma idade acima de 20 anos ")
    return idade       
         
start = True
while start:
    nome = mod_inputs.inp_str("\nDigite seu nome: ")
    idade = valida_idade() 
    peso = mod_inputs.inp_float("Digite seu peso em kg: ")
    altura = mod_inputs.inp_float("Digite sua altura em MT: ")
    imc = calcula(altura,peso)
    classif = classificacao(imc, idade)
    
    print ("\nO nome do Cliente é ",nome)
    print ("A idade é ", idade, " anos")
    print ("Seu peso é ", peso, " kg")
    print ("Sua Altura é ", altura, "MT")
    print ("Seu IMC é", round (imc, 2))
    print ("Você está com: ", classif)
   
    start = mod_sair.finalizar()