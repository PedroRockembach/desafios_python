#desenvolva um programa que leia três comprimentos e diga se elas podem formar um triangulo
# nenhum lado pode ser maior que a soma dos outros dois, nem menor que a diferença.
#inserir outro if

import os 

os.system('cls')

a=float(input('digite um valor -->'))
b=float(input('digite outro valor -->'))
c=float(input('digite o ultimo valor -->'))

if a<=b+c and b<=a+c and c<=a+b:

    print('Pode ser um triangulo')

else: 

    print('Não pode ser um quadrado')