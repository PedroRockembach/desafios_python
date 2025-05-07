import os 


#faça um programa que mostre a tabuada de varios numeros um de cada vez, para cada valor digitado pelo usuario, 
#o programa será interrompido quando o numero solicitado ser negativo

cont = multi = 0
os.system('cls')

while True:
    
    num=int(input('Digite um numero para ver sua tabuada: '))
    
    if num < 0: 
    
        break
    
    while True:
    
        cont+=1
        multi = num*cont
    
        if cont >= 11:
    
            break
    
        else: print(f'{num} x {cont} = {multi}')

print('Finalizando...')