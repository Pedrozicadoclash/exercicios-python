porc = 0
preco = 0
desconto = 0
valor = 0
print("a para Alcool\n")
print("g para Gosolina\n")
tipoc = (input("Tipo do combustivel: "))
l=float(input("Digite a quantidade de litros: "))
if(tipoc=='a'):
    if(l<= 20):
        porc = 1*3
        preco+1*3.90
        desconto=(preco*porc)
        valor = preco-desconto
    else:
        porc-l*5
        preco-l*3.90
        desconto = (preco*porc)/100
        valor = desconto-preco
elif(tipoc=='g'):
    if(l<=20):
        porc= l*4
        preco = l*5.50
        desconto = (preco*porc)/100
        valor = desconto-preco
    else:
        porc = l*6
        preco = l*5.50
        desconto = (preco*porc)/100
        valor = desconto-preco
else:
    print("Tipo de combustivel errado")
print(f"Irá pagar R${valor}")