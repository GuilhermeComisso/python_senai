#Verificar valor

def verificar_numero():
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

numero = verificar_numero()
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é impar")