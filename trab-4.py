S = 1
cont = 0
alterna = True
for i in range(3, 104, 2):
    if alterna:
       S -= 1/(i**3)
       alterna = False
    else:
        S +=1/(i**3)
        alterna = True
    cont += 1

#Saída:
print(f'Numero de termos: {cont}')
print(f'Valor de Pi aproximado: {(S*32)**(1/3)}')