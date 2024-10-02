palavra = input("Digite uma palavra: ")
palarv = palavra.lower().strip().replace('', '')
if(palarv==palarv[::-1]):
    print("É um palindromo")
else:
    print("Não é um palindromo")