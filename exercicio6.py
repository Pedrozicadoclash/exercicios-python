num1= int(input("digite um numero: "))
num2= int(input("digite outro numero: ")) 
oprd= input("Digite um sinal: ")
if(oprd=='+'):
  resultado= num1+num2
  print("a soma dos numeros é: ", resultado)
elif (oprd=='-'): 
  resultado= num1-num2
  print("a subtração dos numeros é: ", resultado)
else:
  print("operador invalido")
