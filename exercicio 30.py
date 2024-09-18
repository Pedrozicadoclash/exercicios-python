num1 = int(input("Digite um número: "))
operador = str(input("digite o operador: "))
num2 = int(input("Digite outro número: "))
if operador== '-':  
    resultado = num1-num2
    print(resultado) 
elif operador=='+':
    resultado = num1+num2
    print(resultado)
elif operador=='*':
    resultado = num1*num2
    print(resultado)
elif operador =='/':
    resultado = num1/num2
    print(resultado)
else:
    print("operador invalido")  

