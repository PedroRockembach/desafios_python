import os 
from random import sample,randint
from time import sleep

os.system('cls')
#crie um programa que crie uma lista com 5 numeros aleatorios e após mostre o maior e o menor valror da lista

tamanho = 5
valores = range(1,10)

print('-='*15)
print('          Metodo 1')
print('-='*15)

sleep(1.2)

numeros = (sample(valores,tamanho))

print(f" ---> {numeros} ")

maior = max(numeros)
menor = min(numeros)

print(f'O maior valor é -> {maior}')
print(f'O menor valor é -> {menor}')

# ou... #

sleep(2)

minimo = float('inf')
maximo = float('-inf')

print('-='*15)
print('         Metodo 2')
print('-='*15)

numeros2 = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f" ---> {numeros2}")

for n in numeros2:
    
    if n > maximo:
        
        maximo = n 
        
    elif n < minimo:
        
        minimo = n
        
print(f'O maior valor é -> {maximo}')
print(f'O menor valor é -> {minimo}')