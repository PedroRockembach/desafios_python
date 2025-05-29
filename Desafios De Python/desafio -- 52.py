import os
from time import sleep
os.system('cls')
#faça um programa que leia um numero e diga ou nao se ele é primo
print('\033[35mPrograma de verificação de números primos\033[m')
sleep(2)
print('Carregando...')
sleep(3)
cont=0
n=int(input('\033[35mDigite um numero para verificar:\033[m '))
for a in range(1,n+1):
    if n / a == n or n / a == 1:
        print(f'\033[32m{a}\033[m',end=' ')
        cont+=1
    elif n % a == 0:
        print(f'\033[33m{a}\033[m',end=' ')  
        cont+=1
    else:
        print(f'\033[31m{a}\033[m',end=' ')
if cont==2:
    print(f'\nO numuero possui apenas \033[32m{cont}\033[m divisores, logo ele é PRIMO')
else:
    print(f'\nO numero possui \033[31m{cont}\033[m divisores, logo ele NÃO É PRIMO')