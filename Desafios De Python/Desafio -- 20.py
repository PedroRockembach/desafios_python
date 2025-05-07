#faça um programa que leia uma entrada de nomes e sorteie em ordem

import os
import random

os.system('cls')

nome1=str(input('\033[1;35mPrimeiro aluno -->\033[m'))
nome2=str(input('\033[1;35mSegundo aluno -->\033[m'))
nome3=str(input('\033[1;35mTerceiro aluno -->\033[m'))
nome4=str(input('\033[1;35mQuarta nome -->\033[m'))

candidatos=nome1,nome2, nome3, nome4

ordem=random.sample((candidatos),4)

print(f'\033[1;34mA ordem para apresentação do trabalho será \033[1;36m{ordem}\033[m')