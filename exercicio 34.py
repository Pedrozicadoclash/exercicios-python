a = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo:")) 
if sexo == 'm':
  result1 = (72.7*a) - 58
  print(f"Seu peso ideal é em média {result1}")
elif sexo =='f':
  result2 = (62.1*a) - 44.7
  print(f"Seu peso ideal é média {result2}")