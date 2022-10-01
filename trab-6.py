def quantidade_de_nuggets():
    while True:
        valor = int(input("Informe a quantidade de nuggets que deseja comprar: "))
        if valor > 0:
            return valor
        print("Quantidade inválida!")


comprar = False
valor = quantidade_de_nuggets()
for a in range((valor // 6) + 1):
    for b in range((valor // 9) + 1):
        for c in range((valor // 20) + 1):
            if (6 * a) + (9 * b) + (20 * c) == valor:
                comprar = True
                print(a, "pacote de 6 nuggets", b, "pacote de 9 nuggets", c, "pacote de 20 nuggets conseguem comprar",
                      valor, "nuggets", sep=" ")

print("Consegue comprar?", comprar, sep=" ")