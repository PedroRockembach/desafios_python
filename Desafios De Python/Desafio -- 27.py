#faça um programa que leia o nome completo de uma pessoa e em seguida mostre o primeiro e o ultimo nome

import os

os.system('cls')

nome=input('digite seu nome completo por favor -->').split()

print(nome[0])
print(nome[len(nome)-1])