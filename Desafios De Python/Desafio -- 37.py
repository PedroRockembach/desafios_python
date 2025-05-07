#faça um programa que leia um numero inteiro e o usuario deve escolher se a base de sua conversão será:
#binario
#hexa
#octal

import os

os.system('cls')

n=int(input('\033[36mEscolha um número inteiro -->\033[m'))

print('''
escolha agora a base de conversão para seu número-->
1->binario
2->octal
3->hexadecimal
\033[31m-=-=-=-=->\033[m''')

ops=int(input('sua escolha:'))

if ops==1:
    print(bin(n)[2:])
elif ops==2:
    print(oct(n)[2:])
elif ops==3:
    print(hex(n)[2:])
else:
    print('opção invalida. Tente novamente')
