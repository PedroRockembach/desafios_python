#faça um programa que leia 3 numeros e diga qual o maior e o meno
import os
import math
os.system('cls')
n1=int(input('Digite um numero -->'))
n2=int(input('Digite outro numero -->'))
n3=int(input('Digite mais um numero -->'))
if n1>n2:
    if n1>n3:
         print(f'{n1} é o maior valor')
         if n3>n2:
             print(f'{n2} é o menor valor') 
         else:
             print(f'{n3} é o menor valor')
    else:
         if n3>n2:
            print(f'{n3} é o maior')
else:   
    if n2>n3:
        print(f'{n2} é o maior valor')
        if n3>n1:
            print(f'{n1} é o menor valor')
        else:
            print(f'{n3} é o menor valor')
    else: 
        print(f'{n3} é o maior valor')
        if n2>n1:
            print(f'{n1} é o menor valor')
        else:
            print(f'{n2} é o menor valor')
#é o rock'n roll