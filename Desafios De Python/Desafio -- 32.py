#crie um programa que descubra se um ano é bissexto ou não

import os

os.system('cls')


a=int(input('Insira um ano e irei descobrir se ele é ano bissexto ou não-->'))

if a%4 == 0 and a%100 != 0 or a%400 == 0:
    
    print('seu ano é BISSEXTO')

else:
     
    print('seu ano NÃO É BISSEXTO')
