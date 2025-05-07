#faça um programa que leia um numero e mostre seu fatorial
import os 
os.system('cls')
n=int(input('Digite um numero para achar seu fatorial: '))
c=n
f=1
while c > 0:
    print(f'{c}',end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c 
    c -= 1
print(f)

#Usando While
#n1 = int(input('Digite um número para saber o fatorial: '))
#f1 = 1
#c1 = n1
#while c1 > 1:
#    f1 *= c1
#    c1 -= 1
#print(f'O resultado de {n1}! é  {f1}')
    