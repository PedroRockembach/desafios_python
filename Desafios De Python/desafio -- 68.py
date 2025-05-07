#programa que joga par ou impar

import os 
import random
from time import sleep

os.system('cls') # limpa o terminal

v=0 

#inicia software
print('-'*20)
print('Jogo de par ou impar')

#inicia jogo

while True:
    
    print('-'*20)
    e=int(input('Escolha seu numero: '))
    
    if e < 1 or e > 10:
        print('⚠️Por favor, digite um valor entre 1 e 10.')
        
        continue # pede o valor mais uma vez( do caralho ta)
    
    jogada=str(input('Qual você é? [P/I]: ')).lower()
    
    if jogada != 'p' and jogada != 'i':
        print('⚠️Entrada inválida, por favor digite P ou I.')
        
        continue
    
    a = random.randint(1,10)

    #se o resto da divisão da soma(entrada do jogador e entrada da maquina) for = 0 quer dizer que é par, logo se o jogador
    #selecionou par ele ganha 
    #se o resto da divisão for diferente de 0 e o jogador selecionou impar, ele ganha, se não estiver nesses casos, ele perde.

    print('-'*20)

    soma=e+a # efetua a soma dos valores
    
    sleep(1.8)
    print(f'A Minha jogada foi {a}...')

    if (soma%2) == 0 and jogada == 'p' or (soma%2) != 0 and jogada == 'i':
        print('🎉 Você ganhou! 🎉')
        print(f'Você já está com {v} vitorías ')
        v+=1
        
    else:
        print('💀 Você perdeu! 💀')
        break
    
    
    # se quiser perguntar para jogar denovo
    #dnv=str(input('Quer jogar mais uma vez?[Y/N]')).lower().strip()
    #if dnv == 'n':
        #break 





