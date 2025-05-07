#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com santo


import os

os.system('cls')

c1=input('escolha o nome de uma \033[36mcidade -->\033[m').strip()

if c1[:5].lower() == 'santo':
    
    print('Sim, começa com santo.')
else:
    
    print('não, não começa com santo')


