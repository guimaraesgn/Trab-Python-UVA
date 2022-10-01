from decimal import Decimal

flamengo = []
vasco = []
fluminense = []
botafogo = []
outros = []


class Entrevista:
    def __init__(self, clube, salario, cidade):
        self.clube = clube
        self.salario = Decimal(salario)
        self.cidade = cidade


def informar_clube_de_futebol():
    while True:
        print("Informe o seu clube de futebol")
        oClube = int(input("1 - Flamengo; 2 - Vasco; 3 - Fluminense; 4 - Botafogo; 5 - Outros: "))
        if 5 >= oClube >= 1:
            return oClube
        print("Número informado é inválido!")


def informar_salario():
    while True:
        salario = Decimal(round(Decimal(input("Informe o seu salário: ")), 2))
        if salario.compare(Decimal('0')) >= 0:
            return salario
        print("Salário informado é inválido!")


def informar_cidade_natal():
    while True:
        print("Informe a sua cidade natal")
        cidade_informada = int(input("1 - Niterói; 2 - Outra: "))
        if 2 >= cidade_informada >= 1:
            return cidade_informada
        print("Número informado é inválido!")


def entrevistar_pessoa():
    while True:
        resultado = int(input("1 - entrevistar; 0 - sair: "))
        if resultado == 0:
            print("Encerrando entrevista!")
            return
        elif resultado == 1:
            entrevistar()
        else:
            print("Número informado é inválido!")


def entrevistar():
    entrevista = Entrevista(informar_clube_de_futebol(), informar_salario(), informar_cidade_natal())
    if entrevista.clube == 1:
        flamengo.append(entrevista)
    elif entrevista.clube == 2:
        vasco.append(entrevista)
    elif entrevista.clube == 3:
        fluminense.append(entrevista)
    elif entrevista.clube == 4:
        botafogo.append(entrevista)
    else:
        outros.append(entrevista)


def calcular_media_salarial(time=[]):
    if len(time) == 0:
        return Decimal('0.0')

    soma = Decimal('0')
    for index in time:
        soma = soma + index.salario
    return Decimal(round(soma / len(time), 2))


def calcular_quantidade_de_pessoas_nascidas_em_niteroi_que_torcem_para_outros():
    quantidade = 0
    for index in outros:
        if index.cidade == 1:
            quantidade += 1
    return quantidade


def calcular_quantidade_de_pessoas_entrevistadas():
    return len(flamengo) + len(vasco) + len(fluminense) + len(botafogo) + len(outros)


entrevistar_pessoa()
print("------------------------")
print("Quantidade de torcedores por clube")
print("Flamengo =", len(flamengo),
      "Vasco =", len(vasco),
      "Fluminense =", len(fluminense),
      "Botafogo =", len(botafogo),
      "Outros =", len(outros),
      sep=" "
)

print("------------------------")
print("Média salarial de torcedores por clube")
print("Flamengo =", calcular_media_salarial(flamengo),
      "Vasco =", calcular_media_salarial(vasco),
      "Fluminense =", calcular_media_salarial(fluminense),
      "Botafogo =", calcular_media_salarial(botafogo),
      "Outros =", calcular_media_salarial(outros),
      sep=" "
)

print("------------------------")
print("Quantidade de pessoas nascidas em Niterói que não torcem para os times sugeridos =",
      calcular_quantidade_de_pessoas_nascidas_em_niteroi_que_torcem_para_outros(),
      sep=" "
)

print("------------------------")
print("Quantidade de pessoas entrevistadas =",
      calcular_quantidade_de_pessoas_entrevistadas(),
      sep=" "
)