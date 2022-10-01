import math
def opeações():
    while True:
        print('-'*30)
        print('Calculadora Python')
        print('-'*30)
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Dividir")
        print("4 - Multiplicar")
        print("5 - Sair")
        operador = int(input('Escolha uma opção: '))
        if operador == 5:
            print("Saindo do programa!")
            exit(0)
        if 4 >= operador >= 1:
            informar_numeros(operador)
        else:
            print("Número informado é inválido!")


def informar_numeros(operador):
    primeiroNumero = int(input("Informe o primeiro número: "))
    segundoNumero = int(input("Informe o segundo número: "))

    if operador == 1:
        print("resultado da soma =", (primeiroNumero + segundoNumero), sep=" ")
    if operador == 2:
        print("resultado da subtração =", (primeiroNumero - segundoNumero), sep=" ")
    if operador == 3:
        if segundoNumero == 0:
            print("divisão por zero é inválido")
        else:
            print("resultado da subtração =", math.trunc((primeiroNumero / segundoNumero)), sep=" ")
    if operador == 4:
        print("resultado da multiplicação =", (primeiroNumero * segundoNumero), sep=" ")

opeações()