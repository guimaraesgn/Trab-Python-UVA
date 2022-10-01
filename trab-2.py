x     = int(input("Digite o valor de x?"))
y     = int(input("Digite o valor de y?"))
cont  = 0
acc   = 0

for i in range(y,x+1,y):
        cont = cont + 1
        acc  = acc + y

print ("divisao=",cont," resto=", x-acc)