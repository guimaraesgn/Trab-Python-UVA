def quantidade_numeros():
    return int(input("Quantos números você quer deseja informar: "))


def numeros_desejados(quantidade_numeros):
    numeros = []

    for i in range(quantidade_numeros):
        numeros.append(int(input("Informe um número: ")))
    return numeros


def somadosQuadados(numeros=[]):
    soma = 0
    for x in numeros:
        soma += (x ** 2)
    return soma


print(
    "A soma total é:",
    somadosQuadados(numeros_desejados(quantidade_numeros())),
    sep=" "
)