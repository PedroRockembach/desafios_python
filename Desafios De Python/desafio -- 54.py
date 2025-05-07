#faça um programa que leia o ano de nascimento de sete pessoas e 
#por fim mostre quantos são maiores e quais são menores de idade

import os 
import datetime

os.system('cls')

data=datetime.date.today().year

maior=menor=0

for i in range(1,8):
    
    idade=int(input(f'\033[34mEm que ano a {i}° pessoa nasceu nasceu?\033[m'))
    
    if data-idade>=18:
        
        print(f'\033[32mVocê é maior de idade, tendo {data-idade} anos\033[m')
        maior+=1
    else:
        
        print(f'\033[31mVocê é menor de idade, tendo apenas {data-idade} anos\033[m')
        menor+=1
        
print(f'Ao todo, temos \033[32m{maior}\033[m pessoas maiores de idade\nE também temos \033[31m{menor}\033[m pessoas menores de idade')

    