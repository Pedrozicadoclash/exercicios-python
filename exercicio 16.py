salario = float(input("Digite seu salario: "))
aumento = int(input("digite seu percentual de aumento: "))
novo_aumento = salario+(salario*aumento/100)-salario
novo_salario = novo_aumento+salario
print("Você teve um aumento de: ",novo_aumento)
print("Seu novo salario é: ",novo_salario)          