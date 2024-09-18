print("Equação de 2 grau")

a = int(input("Informe o valor de 'A': "))
b = int(input("Informe o valor de 'B': "))
c = int(input("Informe o valor de 'C': "))

delta = 0

if(a == 0):
    print("Essa equação não é de segundo grau")
else:
    delta = (b*b) - (4*a) * c
    if (delta < 0):
        print("Essa equação não possui raizes. ")
    elif(delta==0):
        print("Essa equação possui apenas raíz real")
    else:
        print("A equação possui duas raízes")