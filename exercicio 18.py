deposito = float(input("Digite o valor depositado: "))
juros = int(input("digite o juros: "))
rendimento = (juros*deposito/100)
valor_total =juros - rendimento + deposito
print("Você teve um rendimento de: ",rendimento)
print("O valor total é de: ",valor_total)          