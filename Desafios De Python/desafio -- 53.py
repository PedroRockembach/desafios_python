#crie um programa que leia uma frase e detecte se ela é um palindromo
import os 
from time import sleep

os.system('cls')

print('\033[31mBem vindo ao programa de reconhecimemto de palindromos\033[m')
sleep(1)
print('Carregando...')
sleep(1)

frase=str(input('Digite sua frase aqui: ')).strip().lower()

palavra=frase.split()
junto=''.join(palavra)
inverso='' #inverso=junto[::-1] funciona igual esse for

for letra in range(len(junto)-1,-1,-1):
    
    inverso+=junto[letra]
    
print(f'Frase Original:{junto}\nFrase Inversa:{inverso}')

if inverso == junto:
    
    print('\033[32mA frase é um palindromo pois é igual de tras para frente\033[m')
else:
    
    print('\033[31mA frase não é um palindromo\033[m')
    