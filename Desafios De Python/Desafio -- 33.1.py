#identifique o menor e o maior entre 3 valores

import os

os.system('cls')

n1=input('escolha o primeiro numero-->')

n2=input('escolha o segundo numero-->')

n3=input('escolha o terceiro numero-->')

menor=n3

if n1<n2 and n1<n3:
    
    menor = n1
    
if n2<n3 and n2<n1:
    
    menor = n2
maior= n3

if n1>n2 and n1>n3:
    
    maior = n1
    
if n2>n3 and n2>n1:
    
    maior = n2
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')