#faça um programa que leia uma frase e identifique quantas vezes aparece a letra 'a', a primeira e a ultima versão da mes

import os

os.system('cls')

frase=input('Insira uma frase -->').strip().lower()

nA=frase.count('a')
iA2=frase.find('a')
iA=frase.rfind('a')

print(f'O numero de "A" em sua frase é de {nA}')

print(f'o ultimo A na sua frase está na posição {iA}')

print(f'o primeiro A na sua frase está na posição {iA2}')

print(frase)
