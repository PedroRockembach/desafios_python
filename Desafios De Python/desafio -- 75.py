
import os 

os.system('cls')
temnove = 0

#Ler quatro valores e colocar em uma tupla

n1 = int(input("digite um numero inteiro: "))
n2 = int(input("digite um numero inteiro: "))
n3 = int(input("digite um numero inteiro: "))
n4 = int(input("digite um numero inteiro: "))

numeros = (n1,n2,n3,n4)

print('\n---Valores---')
print(numeros)

#Quantas vezes aparece o "9"

for numero in numeros:

    if numero == 9:
        temnove+=1
        
print('\n---Valor Especifico---')
print(f'A tupla possui {temnove} noves')

#Em que posição está o primeiro numero 3

print('\n---Numero Tres---')

if 3 in numeros:
    
    numerotres=numeros.index(3) 
    
    print(f'O primeiro três se encontra na posição {numerotres+1} da tupla')

else:
    
    print('Não possui 3')

#Quais são os numeros pares.

print('\n---Numeros Pares---')

par = False
n = ' '

for numero in numeros:
    
    if numero % 2==0:
        
        par = True
        n+=str(numero)+' -> '
        
if par == True: 
              
    print(f'O numero {n} é par')
    
else:      
    
    print(f'Nenhum destes numeros é par')             
    