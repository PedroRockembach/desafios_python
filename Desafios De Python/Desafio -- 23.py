#fazer um programa que leia um digito ate 9999 e mostre na tela cada digito separadamente

import os

os.system('cls')

num = int(input('digite um numero até 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A unidade é {u}')
print(f'A dezena é {d}')
print(f'A centena é {c}')
print(f'A milhar é {m}')
