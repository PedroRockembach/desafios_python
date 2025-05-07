#jogo da adivinhação V2

import os
import random
from time import sleep

os.system('cls')

print('\033[35mJogaremos um jogo de adivinhação')
sleep(2)
print('Carregando...')
sleep(2)
print('Voce deve advinhar o numero que estou pensando entre 1 e 10\033[m')

t = c = 0

a=random.randint(1,10)

while t != a:
        
    t=int(input('digite sua tentativa: '))
    
    if t==a:
            
            print(f'Parabéns! Você acertou com {c} tentativas')
            
    elif t>a:
            
            print('Menos...Tente denovo')
            
    elif t<a:
            
            print('Mais...Tente denovo')
            
    c+=1    

