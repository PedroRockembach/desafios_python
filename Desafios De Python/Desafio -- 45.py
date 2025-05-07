import os 
import random

os.system('cls')

i=input('''\033[1;36mBom dia, Você quer jogar?\033[m
\033[1;32m-->Sim\033[m
\033[1;31m-->Não\033[m
\033[1;35m-->\033[m''').lower()


escolhas='pedra','papel','tesoura'

ej=random.sample((escolhas),1)

if i == 'sim':

    print('\033[36mCerto! Jogaremos pedra, papel e tesoura.\033[m')
    e=str(input('\033[36mescolha sua jogada, prometo que não irei roubar kk-->\033[m')).lower()

    if ej =='papel' and e == 'tesoura' or ej == 'tesoura' and e == 'pedra' or ej == 'pedra' and e == 'papel':

        print(f'\033[33mParábens!! minha escolha foi {ej} Você ganhou!!')
    elif ej=='tesoura' and e == 'papel' or ej == 'pedra' and e == 'tesoura' or ej == 'papel' and e == 'pedra':

        print(f'\033[31mDERROTADO, minha escolha foi {ej} obvio que eu venci.')

if i =='não':
    print('ok, outra hora jogaremos')
    

   


