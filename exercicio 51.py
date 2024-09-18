num = int(input("Digite um número: "))
if num>=1:
    for i in range(1, num):
        if num % i != 0:
            print(num, "é primo")
        else:
            print(num,"não é primo")
            break
elif num==0:
    print(num,"é zero")
else:
    print(num,"é negativo")