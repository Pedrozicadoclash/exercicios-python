candidato1 = 0
candidato2 = 0
candidato3 = 0
i = 0
voto = 0
eleitores = int(input("Digite o número total de eleitores: "))
for i in range(i, eleitores):
    voto = int(input("Digite quem você votou? "))
    if voto==1:
        candidato1 += 1
    elif voto==2:
        candidato2 += 1
    elif candidato3 ==3:
        candidato3 += 1
    elif voto>=4:
        print("Voto invalido")
        i = i-1
resultado = [(candidato1,"candidato 1")][( candidato2,"candidato 2")][(candidato3,"candidato 3")]
print(f"O vencedor é: {resultado}")
