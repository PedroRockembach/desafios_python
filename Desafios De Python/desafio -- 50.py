#Desenvolva um programa que leia 6 numeros inteiros e mostre a SOMA APENAS DOS PARES se o valor
#digitado for impar o programa deve desconsiderar

import os 
os.system('cls')

s = p=0

for n in range(1,7):
    
    a=int(input(f'\033[36mDigite o {n} numero inteiro: \033[m'))
    
    
    if a%2==0:
        
        p+=1
        s+=a
        
print(f'Você informou {p} numeros pares e sua soma foi {s}')
