#Exercício Python 015: 
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar
# Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

import os

os.system('cls')

kilometro=float(input('quantos \033[4;36mkilometros\033[m foram percorridos pelo carro? -->'))

dias=int(input('e por quantos \033[4;36mdias\033[m foi o aluguel? -->'))

preçokm=kilometro*float(0.15)

aluguel=dias*int(60)+preçokm

print(f'o preço total ficou em \033[1;32m{aluguel}\033[m :polegar_para_cima:',language='pt')