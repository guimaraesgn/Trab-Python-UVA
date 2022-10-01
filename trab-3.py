meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def info_dia():
    return int(input("Informe o dia: "))


def info_mes():
    return int(input("Informe o mes: "))

def info_ano():
    return int(input("Informe o ano: "))


def deve_continuar(dia):
    if dia == 0:
        return False
    return True


def validar_ano(dia, mes, ano):
    if ano < 1000 or ano > 9999:
        print("Ano informado é inválido!")
        return False
    return True


def validar_mes(dia, mes, ano):
    if mes > 12 or mes < 1:
        print("Mês informado é inválido!")
        return False
    return True


def validar_dia(dia, mes, ano):
    if dia < 1:
        print("Dia informado é inválido!")
        return False
    return True


def validar_dia_com_mes(dia, mes, ano):
    quantidade_de_dias_no_mes = meses[mes - 1]

    if mes == 2 and verificar_se_ano_eh_bissexto(ano):
        quantidade_de_dias_no_mes += 1

    if dia > quantidade_de_dias_no_mes:
        print("Dia informado é inválido para o mês informado!")
        return False
    return True


def primeira_data_eh_mais_antiga(primeira_data=[], segunda_data=[]):
    primeira_data_concatenada = concatenar_data(primeira_data)
    segunda_data_concatenada = concatenar_data(segunda_data)

    if segunda_data_concatenada < primeira_data_concatenada:
        print("Primeira data informada deve ser menor do que a segunda data")
        return False
    return True


def concatenar_data(data=[]):
    return int(str(data[0]) + str(data[1]) + str(data[2]))


def data_eh_valida(data=[]):
    validacao = [validar_ano, validar_mes, validar_dia_com_mes]

    for index in range(len(validacao)):
        if not validacao[index](data[2], data[1], data[0]):
            return False
    return True


def verificar_se_ano_eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 != 0:
            return True
        if ano % 400 == 0:
            return True
        return False
    return False


def calcular_total_de_dias(data=[]):
    ano = data[0] - 1
    dias_ano = ano * 365

    aux = 101
    while aux <= ano:
        if verificar_se_ano_eh_bissexto(aux):
            dias_ano += 1
        aux += 1

    mes = data[1] - 1
    dias_mes = 0
    for index in range(mes):
        dias_mes += meses[index]

    if mes > 1 and verificar_se_ano_eh_bissexto(data[0]):
        dias_mes += 1

    return dias_ano + dias_mes + data[2]


def calcular_diferenca_de_dias_entre_as_datas(primeira_data=[], segunda_data=[]):
    return calcular_total_de_dias(segunda_data) - calcular_total_de_dias(primeira_data)


def informar_primeira_data():
    while True:
        print("Informe a primeira data!")
        data = [info_ano(), info_mes(), info_dia()]
        if not deve_continuar(data[2]):
            print("Saindo do programa!")
            exit()
        if data_eh_valida(data):
            return data


def informar_segunda_data(primeira_data=[]):
    while True:
        print("Informe a segunda data!")
        data = [info_ano(), info_mes(), info_dia()]
        if not deve_continuar(data[2]):
            print("Saindo do programa!")
            exit()
        if data_eh_valida(data) and primeira_data_eh_mais_antiga(primeira_data, data):
            return data


while True:
    primeira_data = informar_primeira_data()
    segunda_data = informar_segunda_data(primeira_data)

    print(
        "A diferença de dias entre as datas é de",
        calcular_diferenca_de_dias_entre_as_datas(primeira_data, segunda_data),
        "dias",
        sep=" "
    )