qtd_nums_0_25 = 0
qtd_nums_26_50=0
qtd_nums_51_75=0
qtd_nums_76_100=0
    
while(True): 
     num= int(input("Digite um número maior que 0: "'\n')) 
     if(num >0):
        if(num>=0 and num<=25):
          qtd_nums_0_25 =qtd_nums_0_25 +1
        elif(num>=26 and num<=50):
            qtd_nums_26_50 = qtd_nums_26_50 +1
        elif(num>=51 and num<=75):
            qtd_nums_51_75 = qtd_nums_51_75 +1
        elif(num>=76 and num<=100):
            qtd_nums_76_100 = qtd_nums_76_100 +1
     else:
       break


print(f"O intervalo entre 0 e 25 é: {qtd_nums_0_25}'\n' O intervalo entre 26 e 50 é: {qtd_nums_26_50}'\n' O intervalo entre 51 e 75 é: {qtd_nums_51_75}'\n' O intervalo entre 76 e 100 é: {qtd_nums_76_100}")


