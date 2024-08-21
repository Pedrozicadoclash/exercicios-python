genero = input("Digite uma letra para gênero F=feminino ou M=masculino: ")[0]
genero = genero.lower()
if(genero == 'f'):
    print("O seu gênero é feminino ")
elif(genero == 'm'):
    print("O seu gênero é masculino ")
else:
    print("Gênero invalido")
